<template>
  <div>
    <a-row :gutter="24" type="flex" align="stretch" class="mb-24">
      <a-col
        :span="6"
        v-for="(card, index) in this.cards"
        :key="card.icon + index"
      >
        <WidgetCounter
          :title="card.title"
          :value="card.value"
          :suffix="card.suffix"
          :status="card.status"
          :icon="card.icon"
        ></WidgetCounter>
      </a-col>
    </a-row>
    <a-row :gutter="24">
      <a-col :span="12">
        <a-card
          :bordered="false"
          style="height: 390px"
          class="dashboard-bar-line header-solid mb-24"
        >
          <template #title>
            <h6>过去十天爬虫运行情况</h6>
            <p>今日爬虫运行数量 <span class="text-danger">-1</span></p>
          </template>
          <template #extra>
            <a-badge
              color="secondary"
              class="badge-dot-secondary"
              text="爬虫运行数量"
            />
          </template>
          <ChartBar></ChartBar> </a-card
      ></a-col>
      <a-col :span="12">
        <a-card
          :bordered="false"
          style="height: 390px"
          class="dashboard-bar-line header-solid mb-24"
        >
          <template #title>
            <h6>过去十天侵权资源增长情况</h6>
            <p>已发现网站数量 <span class="text-success">+0.8%</span></p>
          </template>
          <template #extra>
            <a-badge
              color="primary"
              class="badge-dot-primary"
              text="侵权网站"
            />
            <a-badge
              color="primary"
              class="badge-dot-secondary"
              text="侵权电影"
            />
          </template>
          <myChartLine :height="310" :data="lineChartData"></myChartLine>
        </a-card>
      </a-col>
    </a-row>
    <a-row :gutter="24" style="min-height: 470px">
      <a-col :span="16">
        <a-card class="mb-24 card-table">
          <a-table
            :columns="columns"
            :data-source="
              data.slice(pageSize * (current - 1), pageSize * current)
            "
            :pagination="false"
            :row-key="(record) => record.id"
            :loading="loading"
            @change="handleTableChange"
            :customRow="onClickRow"
          >
            <span slot="project" slot-scope="project">
              <a-tag color="orange">
                {{ project }}
              </a-tag>
            </span>
            <span slot="spider" slot-scope="spider">
              <a-tag color="blue">
                {{ spider }}
              </a-tag>
            </span>
            <span slot="status" slot-scope="status">
              <div v-if="status == 1">
                <a-badge status="processing" text="运行中" />
              </div>
              <div v-if="status == 2">
                <a-badge status="warning" text="已关闭" />
              </div>
            </span>
          </a-table>
          <div style="margin-bottom: 15px">
            <a-button
              style="
                margin-left: 20px;
                background-color: rgb(82, 196, 26);
                color: white;
              "
              @click="showModal()"
              >新建任务</a-button
            >
            <a-modal
              v-model="visible"
              width="700px"
              title="创建新任务"
              on-ok="handleOk"
            >
              <template slot="footer">
                <a-button key="back" @click="handleCancel"> 取消 </a-button>
              </template>
              <add-spider @changeVisible="setVisible" />
            </a-modal>
            <a-pagination
              show-quick-jumper
              :current="current"
              :pageSize="pageSize"
              :total="total"
              @change="onChange"
              style="float: right"
            />
          </div>
        </a-card>
      </a-col>
      <a-col :span="8">
        <a-card class="mb-24 card-table">
          <a-descriptions :column="1" bordered>
            <a-descriptions-item label="任务ID" style="height: 200px">
              {{ this.item.id }}
            </a-descriptions-item>
            <a-descriptions-item label="任务名称">
              {{ this.item.job }}
            </a-descriptions-item>
            <a-descriptions-item label="任务种类">
              <a-tag color="orange"> {{ this.item.project }} </a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="爬虫种类">
              <a-tag color="blue"> {{ this.item.spider }} </a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="开始时间">
              {{ this.item.start }}
            </a-descriptions-item>
            <a-descriptions-item label="结束时间">
              {{ this.item.finish }}
            </a-descriptions-item>
            <a-descriptions-item label="运行总时间">
              {{ this.item.runtime }}
            </a-descriptions-item>
            <a-descriptions-item label="Status">
              <div v-if="this.item.status == 1">
                <a-badge status="processing" text="运行中" />
              </div>
              <div v-if="this.item.status == 2">
                <a-badge status="warning" text="已关闭" />
              </div>
            </a-descriptions-item>
            <a-descriptions-item label="页面总数">
              {{ this.item.pages }}
            </a-descriptions-item>
            <a-descriptions-item label="元素数量">
              {{ this.item.items }}
            </a-descriptions-item>
            <a-descriptions-item label="操作类型">
              <div v-if="this.item.status == 1">
                <a-button
                  @click="stopSpider"
                  style="background-color: rgb(250, 219, 20); color: white"
                  >停止任务</a-button
                >
              </div>
              <div v-if="this.item.status == 2">
                <a-button
                  style="background-color: rgb(24, 144, 255); color: white"
                  @click="showAnalyze()"
                  >分析任务</a-button
                >
              </div>
              <a-modal
                v-model="isAnalyze"
                width="700px"
                title="分析任务"
                on-ok="handleOk"
              >
                <NewTask />
                <template slot="footer">
                  <a-button key="back" @click="handleCancelTask">
                    取消
                  </a-button>
                </template>
              </a-modal>
            </a-descriptions-item>
          </a-descriptions>
          <!-- <div style="margin-top:10px; margin-left:10px;">

          </div> -->
        </a-card></a-col
      ></a-row
    >
    <a-row :gutter="24">
      <a-col :span="24" :lg="18" class="mb-24">
        <a-card class="card-calendar" style="padding: 16px; height: 480px">
          <FullCalendar :options="calendarOptions" />
        </a-card>
      </a-col>
      <a-col :span="24" :md="6">
        <!-- Next Event card -->
        <a-card style="height: 480px; background-color: white">
          <CardNextEvents :data="eventsData" class="mb-24"></CardNextEvents>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import axios from "axios";
import AddSpider from "../components/AddSpider.vue";
import "@fullcalendar/core/vdom"; // solves problem with Vite
import FullCalendar from "@fullcalendar/vue";
import dayGridPlugin from "@fullcalendar/daygrid";
import interactionPlugin from "@fullcalendar/interaction";
import CardNextEvents from "../components/Cards/CardNextEvents";
import WidgetCounter from "../components/Widgets/WidgetCounter";
import myChartLine from "../components/Charts/myChartLine";
import ChartLine from "../components/Charts/ChartLine";
import ChartBar from "../components/Charts/ChartBar2";
import NewTask from "../components/TaskForm.vue";

const queryData = (params) => {
  return axios.post("http://localhost:5000/apiRequestSender/query/listJobs");
};

const columns = [
  {
    title: "ID",
    dataIndex: "id",
    width: "10%",
  },
  {
    title: "探测时间",
    dataIndex: "create_time",
    width: "15%",
  },
  // {
  //   title: "任务名称",
  //   dataIndex: "job",
  //   width: "15%",
  // },
  {
    title: "任务种类",
    dataIndex: "project",
    width: "10%",
    scopedSlots: { customRender: "project" },
  },
  {
    title: "爬虫类型",
    dataIndex: "spider",
    width: "10%",
    scopedSlots: { customRender: "spider" },
  },
  {
    title: "页面数量",
    dataIndex: "pages",
    width: "15%",
  },
  {
    title: "电影数量",
    dataIndex: "items",
    width: "15%",
  },
  {
    title: "任务状态",
    dataIndex: "status",
    width: "15%",
    scopedSlots: { customRender: "status" },
  },
];

export default {
  components: {
    NewTask,
    AddSpider,
    FullCalendar,
    CardNextEvents,
    WidgetCounter,
    ChartLine,
    myChartLine,
    ChartBar,
  },
  data() {
    return {
      isAnalyze: false,
      data: [],
      pagination: {},
      loading: false,
      leftAlignId: "",
      columns,
      size: "large",
      current: 1,
      pageSize: 7,
      total: 0,
      item: {},
      loading: false,
      visible: false,
      length: 0,
      jobs: 0,
      lineChartData: {
        labels: [
          "第一天",
          "第二天",
          "第三天",
          "第四天",
          "第五天",
          "第六天",
          "第七天",
        ],
        datasets: [
          {
            label: "侵权电影网站数量",
            yAxisID: "A",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#1890FF",
            borderWidth: 3,
            data: [20366, 21150, 21802, 21870, 22835, 23395, 23587],
            maxBarThickness: 6,
          },
          {
            label: "侵权电影数量",
            yAxisID: "B",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#B37FEB",
            borderWidth: 3,
            data: [
              2017159, 2019794, 2030030, 2106558, 2143017, 2238699, 2258271,
            ],
            maxBarThickness: 6,
          },
        ],
      },
      cards: [
        {
          title: "任务总数",
          value: this.leftAlignId,
          suffix: "+1",
          icon: '<i class="el-icon-position" style="font-size:22px; color:white;"></i>',
        },
        {
          title: "正在运行任务数",
          value: this.jobs,
          suffix: "-1",
          status: "danger",
          icon: '<i class="el-icon-data-line" style="font-size:22px; color:white;"></i>',
        },
        {
          title: "侵权电影网站数量",
          value: 23587,
          suffix: "+192",
          icon: '<i class="el-icon-zoom-in" style="font-size:22px; color:white;"></i>',
        },
        {
          title: "电影侵权次数",
          value: 2258271,
          suffix: "+19572",
          icon: '<i class="el-icon-video-camera" style="font-size:22px; color:white;"></i>',
        },
      ],
      eventsData: [
        {
          id: "5",
          title: "广度式爬虫",
          code: "2022 年 06 月 02 日 上午 00:00",
          iconClass: "text-primary",
          icon: "windows",
          iconBgColor: "rgba(33,82,255,.03)",
        },
        {
          id: "6",
          title: "关键词爬虫",
          code: "2022 年 06 月 03 日 上午 00:00",
          iconClass: "text-primary",
          icon: "bell",
          iconBgColor: "rgba(121,40,202,.03)",
        },
        {
          id: "7",
          title: "广度式爬虫",
          code: "2022 年 06 月 05 日 上午 00:00",
          iconClass: "text-success",
          icon: "book",
          iconBgColor: "rgba(23,173,55,.03)",
        },
        {
          id: "1",
          title: "广度式爬虫",
          code: "2022 年 06 月 08 日 上午 00:00",
          iconClass: "text-danger",
          icon: "calendar",
          iconBgColor: "rgba(234,6,6,.03)",
        },
        {
          id: "2",
          title: "特异性爬虫",
          code: "2022 年 06 月 10 日 上午 00:00",
          iconClass: "text-primary",
          icon: "bell",
          iconBgColor: "rgba(121,40,202,.03)",
        },
        // {
        //   id: "3",
        //   title: "广度式爬虫",
        //   code: "2022 年 06 月 18 日 上午 00:00",
        //   iconClass: "text-success",
        //   icon: "book",
        //   iconBgColor: "rgba(23,173,55,.03)",
        // },
        // {
        //   id: "4",
        //   title: "广度式爬虫",
        //   code: "2022 年 06 月 21 日 上午 00:00",
        //   iconClass: "text-warning",
        //   icon: "car",
        //   iconBgColor: "rgba(245,57,57,.03)",
        // },
        // {
        //   id: "5",
        //   title: "特异性爬虫",
        //   code: "2022 年 06 月 23 日 上午 00:00",
        //   iconClass: "text-primary",
        //   icon: "windows",
        //   iconBgColor: "rgba(33,82,255,.03)",
        // },
      ],
      calendarOptions: {
        plugins: [dayGridPlugin, interactionPlugin],
        contentHeight: "auto",
        initialView: "dayGridMonth",
        selectable: true,
        headerToolbar: {
          start: "title", // will normally be on the left. if RTL, will be on the right
          center: "",
          end: "today prev,next", // will normally be on the right. if RTL, will be on the left
        },
        initialDate: "2022-06-01",
        editable: true,

        events: [
          {
            title: "广度式爬虫",
            start: "2022-06-18",
            end: "2022-06-18",
            className: "bg-warning text-dark",
          },

          {
            title: "广度式爬虫",
            start: "2022-06-21",
            end: "2022-06-22",
            className: "bg-warning text-dark",
          },

          {
            title: "广度式爬虫",
            start: "2022-06-05",
            end: "2022-06-05",
            className: "bg-warning text-dark",
          },

          {
            title: "关键词爬虫",
            start: "2022-06-29",
            end: "2022-06-29",
            className: "bg-success",
          },

          {
            title: "特异性爬虫",
            start: "2022-06-01",
            end: "2022-06-01",
            className: "bg-primary",
          },

          {
            title: "关键词爬虫",
            start: "2022-06-03",
            end: "2022-06-03",
            className: "bg-success",
          },

          {
            title: "广度式爬虫",
            start: "2022-06-08",
            end: "2022-06-10",
            className: "bg-warning text-dark",
          },

          {
            title: "特异性爬虫",
            start: "2022-06-10",
            end: "2022-06-10",
            className: "bg-primary",
          },

          {
            title: "广度式爬虫",
            start: "2022-06-19",
            end: "2022-06-19",
            className: "bg-warning text-dark",
          },

          {
            title: "特异性爬虫",
            start: "2022-06-23",
            end: "2022-06-23",
            className: "bg-primary",
          },

          {
            title: "广度式爬虫",
            start: "2022-06-02",
            end: "2022-06-02",
            className: "bg-warning text-dark",
          },
        ],
      },
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    handleCancelTask(e) {
      this.isAnalyze = false;
    },
    showAnalyze() {
      this.isAnalyze = true;
    },
    setVisible() {
      this.visible = false;
      this.fetch();
    },
    showModal() {
      this.visible = true;
    },
    handleOk(e) {
      this.loading = true;
      setTimeout(() => {
        this.visible = false;
        this.loading = false;
      }, 3000);
    },
    handleCancel(e) {
      this.visible = false;
    },
    stopSpider() {
      for (var i = 0; i < this.data.length; i++) {
        if (this.data[i].id == this.leftAlignId) {
          this.data[i].status = 2;
        }
      }
    },

    selectRow() {
      console.log("11111");
    },

    onChange(current) {
      this.current = current;
    },

    handleTableChange(pagination, filters, sorter) {
      console.log(pagination);
      const pager = { ...this.pagination };
      pager.current = pagination.current;
      this.pagination = pager;
    },

    fetch(params = {}) {
      this.loading = true;
      queryData({
        results: 10,
        ...params,
      }).then(({ data }) => {
        const pagination = { ...this.pagination };
        // Read total count from server
        // pagination.total = data.totalCount;
        pagination.total = 200;
        this.data = [];
        for (const item in data) {
          this.data.push(data[item]);
        }
        this.total = this.data.length;
        for (var i = 0; i < this.data.length; i++) {
          this.data[i].create_time = this.data[i].create_time.split(" ")[0];

          if (this.data[i].status == 1) {
            this.jobs += 1;
          }
          this.cards[1].value = this.jobs;
          switch (this.data[i].project) {
            case "movieCrawler": {
              this.data[i].project = "电影获取";
              if (this.data[i].spider == "universalSpider") {
                this.data[i].spider = "广度式爬虫";
              } else {
                this.data[i].spider = "特异性爬虫";
              }
              break;
            }
            case "siteCrawler": {
              this.data[i].project = "网站获取";
              if (this.data[i].spider == "keywordSpider") {
                this.data[i].spider = "关键词爬虫";
              } else if (this.data[i].spider == "keywordSpider_baidu") {
                this.data[i].spider = "关键词爬虫";
              } else {
                this.data[i].spider = "关键词爬虫";
              }
              break;
            }
            case "splashHtmlCrawler": {
              this.data[i].project = "HTML处理";
              this.data[i].spider = "HTML爬虫";
              break;
            }
          }
        }
        this.data = this.data.sort((a, b) => b.id - a.id);
        this.loading = false;
        this.leftAlignId = this.data[0].id;
        this.length = this.leftAlignId;
        this.cards[0].value = this.length;
        this.item = this.data[0];
        // this.data = data;
        this.pagination = pagination;
      });
    },

    onClickRow(record, index) {
      return {
        style: {
          "background-color": record.id === this.leftAlignId ? "#C0C0C0" : "",
        },
        on: {
          click: () => {
            this.leftAlignId = record.id;
            for (var i = 0; i < this.data.length; i++) {
              if (this.data[i].id == record.id) {
                this.item = this.data[i];
                // console.log("111");
              }
            }
            console.log(record.id);
            console.log(record);
          },
        },
      };
    },
  },
};
</script>

<style lang="css">
.card-display {
  height: 100px;
}
.charts {
  height: 400px;
}
.card-table {
  /* height: 498px; */
}
</style>
