<template>
  <!-- <a-card style="margin: 20px; border-radius: 20px" :hoverable="true"> -->
  <a-form :model="formState" name="validate_other" v-bind="formItemLayout">
    <a-form-item
      name="selectServer"
      label="服务器"
      has-feedback
      :rules="[{ required: true, message: 'Please select your server!' }]"
    >
      <a-select
        v-model:value="formState.selectServer"
        placeholder="Select a server"
      >
        <a-select-option value="localhost:6800">localhost:6800</a-select-option>
      </a-select>
    </a-form-item>

    <a-form-item
      name="project"
      label="项目"
      has-feedback
      :rules="[{ required: true, message: 'Please select your project!' }]"
    >
      <a-select
        v-model:value="formState.project"
        placeholder="Select a project"
        @change="getVersion(), getSpider()"
      >
        <a-select-option value="movieCrawler">movieCrawler</a-select-option>
        <a-select-option value="siteCrawler">siteCrawler</a-select-option>
        <a-select-option value="splashHtmlCrawler"
          >splashHtmlCrawler</a-select-option
        >
      </a-select>
    </a-form-item>

    <a-form-item
      name="_version"
      label="项目版本"
      has-feedback
      :rules="[{ required: true, message: 'Please select your version!' }]"
    >
      <a-select
        v-model:value="formState._version"
        placeholder="Select a version"
      >
        <a-select-option
          v-for="version in versionInfo"
          :key="version"
          :value="version"
          >{{ version }}</a-select-option
        >
      </a-select>
    </a-form-item>

    <a-form-item
      name="spider"
      label="爬虫"
      has-feedback
      :rules="[{ required: true, message: 'Please select your spider!' }]"
    >
      <a-select
        v-model:value="formState.spider"
        placeholder="Select a spider"
        clearable
      >
        <a-select-option
          v-for="spider in spiderInfo"
          :key="spider"
          :value="spider"
          >{{ spider }}</a-select-option
        >
      </a-select>
    </a-form-item>

    <a-form-item name="switch" label="定时任务">
      <a-switch v-model:checked="formState.switch" />
    </a-form-item>

    <a-form-item
      v-show="formState.switch"
      name="action"
      label="方式"
      has-feedback
    >
      <a-select v-model:value="formState.action" placeholder="Select an action">
        <a-select-option value="add">添加任务</a-select-option>
        <a-select-option value="add_fire">添加任务并立即执行</a-select-option>
        <a-select-option value="add_pause">添加任务并暂停</a-select-option>
      </a-select>
    </a-form-item>

    <a-form-item name="name" label="任务名称" v-show="formState.switch">
      <a-input
        v-model:value="formState.name"
        placeholder="textual description of the task(optional)"
      />
    </a-form-item>
    <a-form-item label="运行天数" v-show="formState.switch">
      <a-input
        v-model:value="formState.day"
        placeholder="day (1-31); CAN BE 1st mon OR last sun OF THE MONTH"
      />
    </a-form-item>

    <a-form-item
      name="day_of_Week"
      label="每周运行天数"
      v-show="formState.switch"
    >
      <a-checkbox-group v-model:value="formState['checkbox-group']">
        <a-row>
          <a-col :span="8">
            <a-checkbox value="*" style="line-height: 32px">*</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="mon-fri" style="line-height: 32px"
              >周一至周五</a-checkbox
            >
          </a-col>
          <a-col :span="8">
            <a-checkbox value="mon" style="line-height: 32px">周一</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="tue" style="line-height: 32px">周二</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="wed" style="line-height: 32px">周三</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="thu" style="line-height: 32px">周四</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="fri" style="line-height: 32px">周五</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="sat" style="line-height: 32px">周六</a-checkbox>
          </a-col>
          <a-col :span="8">
            <a-checkbox value="sun" style="line-height: 32px">周日</a-checkbox>
          </a-col>
        </a-row>
      </a-checkbox-group>
    </a-form-item>

    <a-form-item name="hour" label="小时数" v-show="formState.switch">
      <a-input
        v-model:value="formState.hour"
        placeholder="hour (0-23); 9,17,8-20/4 equals to 8,9,12,16,17,20"
      />
    </a-form-item>
    <a-form-item name="minute" label="分钟数" v-show="formState.switch">
      <a-input
        v-model:value="formState.minute"
        placeholder="minute (0-59); defaults to 0, type */10 to fire every 10 minutes"
      />
    </a-form-item>
    <a-form-item :wrapper-col="{ span: 12, offset: 6 }">
      <a-button
        type="primary"
        html-type="submit"
        @click.prevent="onFinish()"
        :loading="iconLoading"
        >提交</a-button
      >
    </a-form-item>
  </a-form>
  <!-- </a-card> -->
</template>


<script>
// import { UploadOutlined, InboxOutlined } from "@ant-design/icons-vue";
export default {
  name: "AddSpider",
  components: {
    // UploadOutlined,
    // InboxOutlined,
  },
  data() {
    return {
      data_post: {},
      versionInfo: [],
      spiderData: {},
      getData: {},
      spiderInfo: [],
      flag: true,
      iconLoading: false,
      formItemLayout: {
        labelCol: {
          span: 6,
        },
        wrapperCol: {
          span: 14,
        },
      },
      formState: {
        // "checkbox-group": ["*"],
        switch: false,
        rate: 3.5,
      },
      day_of_week: "",
      fullscreenLoading: false,
      filename: "",
    };
  },

  methods: {
    enterIconLoading() {
      this.iconLoading = true;
      setTimeout(() => {
        this.iconLoading = false;
        this.message();
        // this.$router.push("/EventHandler");
        this.$emit("changeVisible", false);
      }, 6000);
    },

    openFullScreen1() {
      this.fullscreenLoading = true;
      setTimeout(() => {
        this.fullscreenLoading = false;
        this.message();
        this.$router.push("/EventHandler");
      }, 5000);
    },

    message() {
      this.$notify({
        title: "提交任务成功",
        message: "您已经成功提交了一个爬取任务",
        type: "success",
      });
    },

    run_spider(filename) {
      this.axios
        .post(
          "http://localhost:5000/apiRequestSender/query/runSpider",
          {
            filename: filename,
          },
          {
            headers: {
              "Content-Type": "application/json;charset=utf-8",
            },
            withCredentials: true,
          }
        )
        .then((response) => {
          // console.log(response.data);
        });
    },

    check(values) {
      this.axios
        .post(
          "http://localhost:5000/apiRequestSender/query/checkSpider",
          {
            ...values,
          },
          {
            headers: {
              "Content-Type": "application/json;charset=utf-8",
            },
            withCredentials: true,
          }
        )
        .then((response) => {
          // console.log(response);
          this.filename = response.data.filename;
          this.run_spider(this.filename);
        });
    },

    //axios获取数据
    getVersionResponse(project) {
      //   console.log("2");
      this.axios
        .post(
          "http://localhost:5000/apiRequestSender/query/listVersions",
          {
            param: project,
          },
          {
            headers: {
              "Content-Type": "application/json;charset=utf-8",
            },
            withCredentials: true,
          }
        )
        .then((response) => {
          console.log("response", response);
          this.getData = response;
          //   return response;
          console.log("111:", this.getData);
          for (var i = 0; i < this.getData.data.versions.length; i++) {
            this.versionInfo.push(this.getData.data.versions[i]);
          }
          //   console.log(this.versionInfo);
        });
    },

    getVersion() {
      this.getVersionResponse(this.formState.project);
    },

    async getSpiderResponse(spider) {
      await this.axios
        .post(
          "http://localhost:5000/apiRequestSender/query/listSpiders",
          {
            param: spider,
          },
          {
            headers: {
              "Content-Type": "application/json;charset=utf-8",
            },
            withCredentials: true,
          }
        )
        .then((response) => {
          this.spiderData = response;
          for (var i = 0; i < this.spiderData.data.spiders.length; i++) {
            this.spiderInfo.pop();
          }
          this.flag = false;
          //   this.formState.spider = [];
          for (var i = 0; i < this.spiderData.data.spiders.length; i++) {
            this.spiderInfo.push(this.spiderData.data.spiders[i]);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },

    getSpider() {
      var response = this.getSpiderResponse(this.formState.project);
    },

    onFinish() {
      if (this.formState["checkbox-group"] === undefined) {
        this.day_of_week = undefined;
      } else {
        for (var i = 0; i < this.formState["checkbox-group"].length; i++) {
          if (i == 0) {
            this.day_of_week = this.formState["checkbox-group"][i];
          } else {
            this.day_of_week =
              this.day_of_week + "," + this.formState["checkbox-group"][i];
          }
        }
      }

      if (this.formState.switch == true) {
        this.data_post = {
          project: this.formState.project,
          version: "default: the latest version",
          spider: this.formState.spider,
          action: this.formState.action,
          task_id: "0",
          trigger: "cron",
          name: this.formState.name,
          day: this.formState.day,
          week: this.formState.week,
          day_of_week: this.day_of_week,
          hour: this.formState.hour,
          minute: this.formState.minute,
          second: "0",
          start_date: "",
          end_date: "",
          timezone: "Asia/Shanghai",
          jitter: "0",
          misfire_grace_time: "600",
          coalesce: "True",
          max_instances: "1",
        };
      } else {
        this.data_post = {
          project: this.formState.project,
          version: "default: the latest version",
          spider: this.formState.spider,
        };
      }

      console.log(this.data_post);
      this.check(this.data_post);
      this.enterIconLoading();
      // this.openFullScreen1();
    },
  },
};
</script>