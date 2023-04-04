import torch
from rumor_model.model import SimilarityModule, DetectionModule
from transformers import BertModel, BertTokenizer
from torchvision import models, transforms
from PIL import Image
import requests
from database.utils import *
from io import BytesIO

# Configs
# DEVICE = "cuda:0"
NUM_WORKER = 1
DEVICE = "cpu"
BATCH_SIZE = 64
LR = 1e-3
L2 = 0  # 1e-5
NUM_EPOCH = 100


class TextClassifier(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bert = BertModel.from_pretrained('bert-base-uncased')
        self.fc = torch.nn.Linear(self.bert.config.hidden_size, 30 * 200)

    def forward(self, input_ids, attention_mask):
        outputs = self.bert(input_ids, attention_mask)
        pooled_output = outputs[1]
        logits = self.fc(pooled_output)
        logits = logits.view(-1, 30, 200)
        return logits


def text_to_input(text):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    inputs = tokenizer(text, return_tensors='pt', padding=True, truncation=True)

    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    model = TextClassifier()
    outputs = model(input_ids, attention_mask)

    return outputs.detach()


def image_to_input(image_url):
    proxy = {
        'http': '127.0.0.1:7890',
        'https': '127.0.0.1:7890'
    }

    response = requests.get(image_url, proxies=proxy)
    image = Image.open(BytesIO(response.content))

    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    model = models.resnet34(pretrained=True)
    model = torch.nn.Sequential(*list(model.children())[:-1])
    model.eval()

    image = transform(image).unsqueeze(0)
    output = model(image)
    batchsize = 1
    output = output.view(batchsize, -1)
    return output.detach()


def test(text, image_url):
    # ---  Load Config  ---
    device = torch.device(DEVICE)

    # --- Data Preprocessing ---
    text = text_to_input(text)
    image = image_to_input(image_url)
    # text = text
    # image = image_url

    similarity_module = SimilarityModule()
    detection_module = DetectionModule()
    similarity_module.load_state_dict(torch.load('rumor_model/models/similarity_model.pth', map_location=torch.device('cpu')))
    detection_module.load_state_dict(torch.load('rumor_model/models/detection_model.pth', map_location=torch.device('cpu')))

    similarity_module.eval()
    detection_module.eval()
    device = torch.device(DEVICE)


    with torch.no_grad():
        text = text.to(device)
        image = image.to(device)

        # ---  Detection  ---
        text_aligned, image_aligned, _ = similarity_module(text, image)
        pre_detection = detection_module(text, image, text_aligned, image_aligned)
        probability = torch.sigmoid(pre_detection)
        # print(probability)
        return probability.tolist()

if __name__ == '__main__':
    # result = text_to_input('This is a test input.')
    # print(result.shape)
    # result = image_to_input('http://pbs.twimg.com/media/FswSVn-X0AAmLhT.jpg')
    # print(result.shape)
    result = query_tweet(0, 20)
    print(result[0])
    # test('I am a genius in playing games!', 'https://pbs.twimg.com/media/FsoIYE6aUAIRj9G.jpg')
    # train_sample = torch.load('./test_sample.pt')
    # text, image, label = train_sample
    # item = 8
    # test(text[item:item+1, :, :], image[item:item+1, :])
    # print(label)
