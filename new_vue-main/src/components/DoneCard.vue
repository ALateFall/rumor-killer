<template>
  <a-card
    style="width: 100%; border-radius: 10px"
    :body-style="{ padding: '0px' }"
    :hoverable="true"
    :bordered="false"
  >
    <a-row class="first-row">
      <a-col :span="6" style="text-align: center">
        <!-- <i
          class="el-icon-lx-notice grid-con-icon"
          style="max-height: 100px"
        ></i> -->
        <a-icon type="schedule" class="grid-con-icon"
          style="max-height: 100px; margin-left:20px;"/>
      </a-col>
      <a-col
        :span="18"
        style="text-align: center; margin-top: 15px; margin-bottom: 15px"
      >
        <b style="font-size: 19px">{{ TaskName }}</b>
        <br />
        <br />
        任务状态：已完成
      </a-col>
      <!-- <a-divider /> -->
    </a-row>

    <a-row style="margin-top: 10px; margin-bottom: 10px; margin-left: 40px">
      <a-button
        style="background-color: rgb(240, 230, 140, 0.3); margin-left: 5px;"
        @click="deleteTimer(), $emit('func', { TaskName })"
      >
        <!-- <delete-outlined style="font-size: 15px" />  -->
        <a-icon type="delete" style="font-size: 15px"/>删除任务
      </a-button>
      <a-button
        style="background-color: rgb(135, 206, 250, 0.3); margin-left:20px;"
        @click="routeTo()"
      >
        <!-- <bar-chart-outlined style="font-size: 15px" /> 查看结果 -->
        <a-icon type="bar-chart" style="font-size: 15px"/>查看结果
      </a-button>
    </a-row>
  </a-card>
</template>

<script>
// import {
//   QuestionCircleOutlined,
//   PoweroffOutlined,
//   RedoOutlined,
//   DeleteOutlined,
//   BarChartOutlined,
// } from "@ant-design/icons-vue";
// import { reactive, inject,ref } from "vue";
// import {useRouter} from "vue-router";
export default {
  name: "DoneCard",
  // components: {
  //   QuestionCircleOutlined,
  //   PoweroffOutlined,
  //   RedoOutlined,
  //   BarChartOutlined,
  //   DeleteOutlined
  // },
  emits: ['func'],
  props: ["TaskName"],
  data(){
    return {
      flag:true,
    }
  },
  methods:{
    deleteTimer(){
        this.axios.post("http://localhost:5000/apiRequestSender/query/deleteTimer",{
            name: this.TaskName,
        }).then(function(response){
            console.log(response);
        })
    },
    routeTo(){
        this.$router.push('/eventresult?task='+this.TaskName);
    }
  }
};
</script>

<style scoped>
.grid-con-icon {
  font-size: 60px;
  margin-top: 20px;
  margin-left: 25px;
  color: black;
}
.first-row {
  background-color: rgb(144, 238, 144, 0.4);
  border-radius: 10px 10px 0px 0px;
}
</style>