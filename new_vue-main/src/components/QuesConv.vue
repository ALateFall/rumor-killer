<template>
  <div>
    <a-row>
      <a-col :span="10" :offset="1"></a-col>
      <a-col :span="10" :offset="1">
        <div style="margin-top: 50px; float: right">
          <div
            style="
              margin-right: 20px;
              margin-top: 15px;
              min-height: 40px;
              min-width: 20px;
              float: left;
              border-radius: 20px;
              background-color: rgb(135, 206, 250, 1);
              word-wrap: break-word;
            "
          >
            <!-- min-height -->
            <div
              style="
                margin-left: 10px;
                margin-top: 10px;
                margin-right: 10px;
                margin-bottom: 10px;
              "
            >
              <div v-html="this.question"></div>
            </div>
          </div>
          <a-avatar
            style="width: 70px; height: 70px; float: left"
            :src="queURL"
          />
        </div>
      </a-col>
    </a-row>
  </div>
</template>
<script>
import queURL from "../assets/img/que.png";
export default {
  name: "QuesConv",
  props: ["question"],
  data() {
    return {
      queURL: queURL,
    };
  },
};
</script>

<style>
</style>