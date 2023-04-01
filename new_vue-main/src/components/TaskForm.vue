<template>
  <a-form-model
    ref="ruleForm"
    :model="form"
    :rules="rules"
    :label-col="labelCol"
    :wrapper-col="wrapperCol"
  >
    <a-form-model-item ref="name" label="任务名称" prop="name">
      <a-input
        v-model="form.name"
        @blur="
          () => {
            $refs.name.onFieldBlur();
          }
        "
      />
    </a-form-model-item>
    <a-form-model-item label="分析方式" prop="resource">
      <a-radio-group v-model="form.resource">
        <a-radio value="1"> 深度分析 </a-radio>
        <a-radio value="2"> 浅度分析 </a-radio>
      </a-radio-group>
    </a-form-model-item>
    <a-form-model-item :wrapper-col="{ span: 14, offset: 4 }">
      <a-button type="primary" @click="onSubmit" :loading="loading">
        提交任务
      </a-button>
    </a-form-model-item>
  </a-form-model>
</template>
<script>
export default {
  data() {
    return {
      loading: false,
      labelCol: { span: 4 },
      wrapperCol: { span: 14 },
      other: "",
      form: {
        name: "",
        resource: "",
      },
      rules: {
        name: [
          {
            required: true,
            message: "请输入任务名称！",
            trigger: "blur",
          },
        ],
        resource: [
          {
            required: true,
            message: "Please select activity resource",
            trigger: "change",
          },
        ],
      },
    };
  },
  methods: {
    openNotificationSuccess(name) {
      this.$notification["success"]({
        message: "创建任务成功！",
        description: "等待任务完成后即可查看详细信息",
      });
    },
    onSubmit() {
      this.$refs.ruleForm.validate((valid) => {
        if (valid) {
            this.loading = true;
          var name = "";
          if (this.form.resource == "1") {
            name = "深度分析任务-" + this.form.name;
          } else {
            name = "浅度分析任务-" + this.form.name;
          }
          this.axios
            .post("http://localhost:5000/apiRequestSender/query/setTimer", {
              name: name,
              second: 5000,
            })
            .then((response) => {
                setTimeout(()=>{
                    this.openNotificationSuccess();
                    this.$router.push("/taskstatus");
                },1000);
            });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    resetForm() {
      this.$refs.ruleForm.resetFields();
    },
  },
};
</script>
