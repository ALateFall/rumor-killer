<template>
  <a-form-model ref="ruleForm" :model="form" :rules="rules">
    <a-form-model-item ref="email" label="邮箱" prop="email">
      <a-input v-model="form.email" placeholder="请输入邮箱..." />
    </a-form-model-item>
    <a-form-model-item ref="username" label="用户名" prop="username">
      <a-input v-model="form.username" placeholder="请输入用户名..." />
    </a-form-model-item>
    <a-form-model-item ref="password" label="密码" prop="password">
      <a-input-password v-model="form.password" placeholder="请输入密码..." />
    </a-form-model-item>
    <a-form-model-item label="是否可用" prop="ban">
      <a-switch v-model="form.ban" />
    </a-form-model-item>
    <a-form-model-item label="所属用户组" prop="group">
      <a-radio-group v-model="form.group">
        <a-radio value="1"> 执法监管人员 </a-radio>
        <a-radio value="2"> 版权拥有者 </a-radio>
      </a-radio-group>
    </a-form-model-item>
    <a-form-model-item :wrapper-col="{ span: 14, offset: 4 }">
      <a-button type="primary" @click="onSubmit" :loading="iconLoading">
        提交
      </a-button>
      <a-button style="margin-left: 10px" @click="resetForm"> 重置 </a-button>
    </a-form-model-item>
  </a-form-model>
</template>
<script>
export default {
  data() {
    return {
      iconLoading: false,
      form: {
        email: "",
        username: "",
        password: "",
        ban: true,
        group: "2",
      },
      rules: {
        email: [
          {
            required: true,
            pattern:
              /^[A-Za-z\d]+([-_.][A-Za-z\d]+)*@([A-Za-z\d]+[-.])+[A-Za-z\d]{2,4}$/,
            message: "请输入正确的邮箱！",
            trigger: "change",
          },
        ],
        username: [
          {
            required: true,
            message: "请输入用户名！",
            trigger: "change",
          },
          {
            min: 8,
            max: 20,
            message: "用户名长度必须在8-20之间！",
            trigger: "change",
          },
        ],
        password: [
          {
            required: true,
            message: "请输入密码！",
            // trigger: "change",
          },
          {
            min: 8,
            max: 20,
            message: "密码长度必须在8-20之间！",
            // trigger: "change",
          },
        ],
        ban: [
          {
            required: true,
            message: "请选择！",
          },
        ],
        group: [
          {
            required: true,
            message: "请选择所属用户组！",
          },
        ],
      },
    };
  },
  methods: {
    message() {
      this.$notify({
        title: "新建用户成功",
        message: "您已经成功新建了一个用户！",
        type: "success",
      });
    },
    onSubmit() {
      this.$refs.ruleForm.validate((valid) => {
        var form = JSON.parse(JSON.stringify(this.form));
        if (valid) {
          this.iconLoading = true;
          if (form.ban == true) {
            form.ban = "0";
          } else {
            form.ban = "1";
          }
          if (form.group == "2") {
            form.group = "normal";
          } else {
            form.group = "super";
          }
          var param = {
            username: form.username,
            password: form.password,
            email: form.email,
            ban: form.ban,
            group: form.group,
          };
          console.log(param);
          this.axios
            .post("http://localhost:5000/manage/user/addUser", param)
            .then((response) => {
              setTimeout(() => {
                this.message();
                this.$emit("changeVisible", false);
              }, 1000);
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
