<template>
  <a-row style="">
    <a-col :span="11" style="margin-top: 30px">
      <a-card
        style="
          background-color: white;
          width: 100%;
          border-radius: 20px;
          min-height: 600px;
        "
        :hoverable="true"
      >
        <QAWelcome />
        <transition-group tag="">
          <div v-for="(item, index) in this.conv" :key="item + index">
            <Conversation :words="item.words" :flag="item.flag" />
          </div>
        </transition-group>

        <div
          style="
            margin-top: 100px;
            margin-left: 100px;
            margin-right: 100px;
            margin-bottom: 30px;
          "
        >
          <a-input-search
            v-model:value="value"
            placeholder="请输入您的问题"
            enter-button="发送"
            show-count
            :maxLength="20"
            @search="onSearch"
          />
        </div>
      </a-card>
    </a-col>
    <a-col :span="12" style="margin-top: 30px; margin-left: 30px">
      <a-card
        style="
          background-color: white;
          width: 100%;
          border-radius: 20px;
          height: 600px; ;
        "
        :hoverable="true"
      >
        <div id="viz" class="neojs"></div>
      </a-card>
    </a-col>

    <a-modal v-model="visible" width="700px" title="详细信息">
      <template slot="footer">
        <a-button key="back" @click="handleCancel">返回</a-button>
      </template>
      <a-table :columns="columns" :data-source="data"> </a-table>
    </a-modal>
  </a-row>
</template>

<script>
import * as NeoVis from "neovis.js";
import Conversation from "../components/Conversation.vue";
import QAWelcome from "../components/QAWelcome.vue";
export default {
  components: { Conversation, QAWelcome },
  data() {
    return {
      visible: false,
      value: "",
      conv: [],
      data: [],
      viz: null,
      columns: [
        {
          title: "网站标题",
          key: "title",
          dataIndex: "title",
        },
        {
          title: "网站Domain",
          key: "domain",
          dataIndex: "domain",
        },
      ],
    };
  },

  methods: {
    draw() {
      var config = {
        container_id: "viz",
        server_url: "bolt://localhost:7687",
        server_user: "neo4j",
        server_password: "1234",
        labels: {
          //"Character": "name",
          // Character: {
          //   caption: "name",
          //   size: "pagerank",
          //   community: "community",
          //   //"sizeCypher": "MATCH (n) WHERE id(n) = {id} MATCH (n)-[r]-() RETURN sum(r.weight) AS c"
          // },
          Domain: {
            caption: "name",
            size: 2,
            community: "community",
          },
          Cluster: {
            caption: "name",
            size: 1,
          },
          Movie: {
            size: 1,
          },
        },
        relationships: {
          has_movie: {
            thickness: "weight",
            caption: true,
          },
        },
        //查询节点的语句，写成你们的
        initial_cypher:
          "match p=(c:Cluster)-[:in_cluster]-(d:Domain) where c.name='2248' return p",
      };
      this.viz = new NeoVis.default(config);
      this.viz.render();
    },
    onSearch(searchValue) {
      this.value = "";
      // console.log("use value", searchValue);

      this.getConversation(searchValue);
    },
    handleCancel() {
      this.visible = false;
    },
    getConversation(que) {
      this.conv.push({
        flag: 1,
        words: que,
      });
      if (que == "哪一个类里面的侵权电影网站最多") {
        this.draw();
        setTimeout(
          this.axios
            .get("http://localhost:8080/records.json")
            .then((response) => {
              console.log(response.data[0].n.end);
              for (var i = 0; i < response.data.length; i++) {
                this.data.push({
                  key: i + 1,
                  title: response.data[i].n.end.properties.Title,
                  domain: response.data[i].n.end.properties.name,
                });
              }
              console.log(this.data);
              this.conv.push({
                flag: 0,
                words:
                  "2248类里面的侵权电影网站最多，共有48个电影网站。您可以通过右方的可视化知识图谱查看。",
              });
              this.visible = true;
            }),
          20000
        );
      } else {
        this.axios
          .post("http://localhost:5000/apiRequestSender/query/QASystem", {
            param: que,
          })
          .then((response) => {
            console.log(response);
            var temp = response.data.data.str;
            if (temp.length > 400) {
              temp = temp.slice(0, 400);
              temp += "...<br/>您还可以访问我们的知识图谱页面查看更多信息。";
            }
            this.conv.push({
              words: temp,
              flag: 0,
            });

            // console.log(response.data.data.str);
          });
      }
    },
  },
};
</script>

<style scoped>
.v-item {
  list-style-type: none;
  /**
	 * 可以在v-enter-active和v-move中分别用transition过渡，也可以在item中用transition，包含了这两项
	 * 要用all不用transform，有可能是因为splice删除效果不是transform
	 */
  /* transition: all 1s; */
  
}
.v-enter-active {
  transition: all 1s;
}
#viz {
  height: 600px;
  width: 100%;
}
.v-move {
  /* transition: all 1s; */
}
.v-enter,
.v-leave-to {
  opacity: 0;
  transform: translateY(20px);
}
.v-leave-active {
  position: absolute;
}
</style>
