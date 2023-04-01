<template>
  <div>
    <a-row style="min-height: 100px">
      <a-col>
        <a-card
          class="mb-24 card-table dashboard-bar-line header-solid"
          style="padding: 16px"
        >
          <a-button
            style="background-color: rgb(24, 144, 255); color: white"
            @click="showModal"
            >新增用户</a-button
          >
          <a-modal
            v-model="visible"
            title="添加用户"
            on-ok="handleOk"
            width="700px"
          >
            <template slot="footer">
              <a-button key="back" @click="handleCancel"> 取消 </a-button>
            </template>
            <new-user @changeVisible="setVisible"></new-user>
          </a-modal>
          <!-- <a-button style="background-color:rgb(24, 144, 255); color:white">用户</a-button> -->
          <a-table
            :columns="columns"
            :row-key="(record) => record.email"
            :data-source="data"
            :pagination="pagination"
            :loading="loading"
            @change="handleTableChange"
          >
            <template slot="operation" slot-scope="text, record">
              <a-popconfirm
                v-if="data.length"
                title="确定要删除吗？"
                ok-text="确定"
                cancel-text="取消"
                @confirm="() => onDelete(record.email)"
              >
                <a-button size="small" type="danger">删除</a-button>
              </a-popconfirm>
              
            </template>
            <span slot="group" slot-scope="group">
              <a-tag
                :color="
                  group == '管理员'
                    ? 'red'
                    : group == '执法监管人员'
                    ? 'orange'
                    : 'blue'
                "
              >
                {{ group }}
              </a-tag>
            </span>
            <span slot="ban" slot-scope="ban">
              <a-tag :color="ban == '可用' ? 'geekblue' : 'gold'">
                {{ ban }}
              </a-tag>
            </span>

          </a-table></a-card
        >
      </a-col>
      <a-col> </a-col>
    </a-row>
  </div>
</template>

<script>
import axios from "axios";
import NewUser from "../components/NewUser.vue";
const queryData = (params) => {
  return axios.post("http://localhost:5000/user/getUserInPage", {
    start: 0,
    count: 100,
  });
};
const columns = [
  {
    title: "序号",
    dataIndex: "id",
    width: "10%",
    // scopedSlots: { customRender: "name" },
  },
  {
    title: "邮箱",
    dataIndex: "email",
    width: "15%",
    // scopedSlots: { customRender: "name" },
  },
  {
    title: "用户名",
    dataIndex: "username",
    // filters: [
    //   { text: "Male", value: "male" },
    //   { text: "Female", value: "female" },
    // ],
    width: "15%",
  },
  {
    title: "权限组",
    dataIndex: "group",
    sorter: (a, b) =>
      a.group.toString().charCodeAt(0) - b.group.toString().charCodeAt(0),
    // filters: [
    //   { text: "Male", value: "male" },
    //   { text: "Female", value: "female" },
    // ],
    scopedSlots: { customRender: "group" },
    width: "15%",
  },
  {
    title: "是否可用",
    dataIndex: "ban",
    sorter: (a, b) => a.ban - b.ban,
    scopedSlots: { customRender: "ban" },
    // filters: [
    //   { text: "Male", value: "male" },
    //   { text: "Female", value: "female" },
    // ],
    width: "10%",
  },
  {
    title: "操作",
    dataIndex: "operation",
    scopedSlots: { customRender: "operation" },
    width: "20%",
  },
];

export default {
  components: {
    NewUser,
  },
  data() {
    return {
      data: [],
      pagination: {},
      loading: false,
      visible: false,
      columns,
    };
  },
  mounted() {
    this.fetch();
  },
  methods: {
    setVisible(data) {
      this.visible = data;
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

    onDelete(key) {
      const data = [...this.data];
      this.data = data.filter((item) => item.email !== key);
      axios
        .post("http://localhost:5000/manage/user/delUser", {
          email: key,
        })
        .then((response) => {
          this.fetch();
        });
    },

    handleTableChange(pagination, filters, sorter) {
      console.log(pagination);
      const pager = { ...this.pagination };
      pager.current = pagination.current;
      pager.defaultPageSize = 10;
      this.pagination = pager;
      this.fetch();
    },
    fetch() {
      this.loading = true;
      queryData().then(({ data }) => {
        const pagination = { ...this.pagination };
        // Read total count from server
        // pagination.total = data.totalCount;
        // pagination.total = 200;
        this.loading = false;
        this.data = data.data;
        for (var i = 0; i < this.data.length; i++) {
          this.data[i]["id"] = i + 1;
          if (this.data[i].group == "normal") {
            this.data[i].group = "版权拥有者";
          } else if (this.data[i].group == "super") {
            this.data[i].group = "执法监管人员";
          } else if (this.data[i].group == "admin") {
            this.data[i].group = "管理员";
          }

          if (this.data[i].ban == "0") {
            this.data[i].ban = "可用";
          } else {
            this.data[i].ban = "已停用";
          }
        }

        console.log(this.data);
        this.pagination = pagination;
      });
    },
  },
};
</script>

<style>
/* .ant-modal-body{
    width:500px;
} */
</style>