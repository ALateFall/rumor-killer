<template>
  <a-row>
    <a-col :span="10" :offset="1">
      <div style="margin-top: 30px">
        <a-row>
          <a-col :span="6">
            <a-avatar style="width: 70px; height: 70px; float: left" :src="ans"
          /></a-col>
          <a-col :span="18">
            <div
              style="
                margin-left: 20px;
                margin-top: 15px;
                width: 380px;
                min-height: 20px;
                float: left;
                border-radius: 20px;
                background-color: rgb(254,242,204,0.5);
                word-wrap: break-word;
              "
            >
              <div
                style="
                  margin-left: 10px;
                  margin-top: 10px;
                  margin-right: 10px;
                  margin-bottom: 10px;
                "
              >
                欢迎来到 Piracy Spy --
                知识产权侵权保护溯源系统，我是您的智能助理。
              </div>
            </div></a-col
          >
        </a-row>
      </div>
    </a-col>
    <a-col :span="10" :offset="1"></a-col>
  </a-row>
</template>

<script>
import ansURL from "../assets/img/ans.png";
export default {
  name: "QAWelcome",
  data() {
    return {
      ans: ansURL,
    };
  },
};
</script>

<style>
</style>