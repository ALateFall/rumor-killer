<template>
  <a-card
    style="width: 100%; border-radius: 10px"
    :body-style="{ padding: '0px' }"
    :hoverable="true"
    :bordered="false"
  >
    <a-row class="first-row">
      <a-col :span="6" style="text-align: center">
        <a-icon
          type="loading"
          class="grid-con-icon"
          style="max-height: 100px"
        />
        <!-- <dv-loading
          class="grid-con-icon"
          style="max-height: 100px; font-color:black;"
        ></dv-loading> -->
      </a-col>
      <a-col
        :span="18"
        style="text-align: center; margin-top: 15px; margin-bottom: 15px"
      >
        <b style="font-size: 19px">{{ TaskName }}</b>
        <br />
        <br />
        任务状态：分析中
      </a-col>
      <!-- <a-divider /> -->
    </a-row>

    <a-row style="margin-top: 10px; margin-bottom: 10px; margin-left: 40px">
      <a-button
        style="background-color: rgb(127, 255, 170, 0.3); margin-left: 5px"
      >
        <!-- <question-circle-outlined  />  -->
        <!-- <QuestionCircleOutlined /> -->
        <a-icon type="question-circle" style="font-size: 15px" />查看任务
      </a-button>

      <a-button
        style="background-color: rgb(255, 192, 203, 0.3); margin-left: 20px"
      >
        <!-- <poweroff-outlined style="font-size:15px;" /> 中止任务 -->
        <a-icon type="poweroff" style="font-size: 15px" /> 中止任务
      </a-button>
    </a-row>
  </a-card>
</template>

<script>
// import { QuestionCircleOutlined, PoweroffOutlined } from "@ant-design/icons-vue";
export default {
  name: "WorkingCard",
  // components: {
  //   QuestionCircleOutlined,
  //   PoweroffOutlined
  // },
  props: ["TaskName"],
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
  background-color: rgb(135, 206, 250, 0.4);
  border-radius: 10px 10px 0px 0px;
}
</style>