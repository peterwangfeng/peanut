<template>
  <div class="container-fluid">
    <div class="text-center" style="color: #42d5f6">
      <span class="title">绩效工资分析系统</span>
    </div>
    <div class="login">
      <p>登&nbsp;录</p>
      <div class="login-content" v-loading="loading" element-loading-text="正在登录中,请稍后..." :lock="true">
        <div class="form-horizontal">
          <div class="form-group">
            <label for="userName" class="col-sm-3 col-md-3 col-xs-3 control-label">用户名</label>
            <div class="col-sm-9 col-md-9 col-xs-9">
              <input v-model="user.name" type="text" class="form-control" id="userName" placeholder="请输入用户名">
            </div>
          </div>
          <div class="form-group">
            <label for="inputPassword" class="col-sm-3 col-md-3 col-xs-3 control-label">密&#x3000;码</label>
            <div class="col-sm-9 col-xs-9 col-md-9">
              <input v-model="user.password" type="password" class="form-control" id="inputPassword"
                     placeholder="请输入密码">
            </div>
          </div>
          <div class="form-group">
            <div class="col-sm-12 col-xs-12 col-md-12 col-lg-12">
              <el-button type="primary" size="large" @click="login">登&nbsp;录</el-button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import * as api from '../api/api';
  import URL from '../api/url';
  export default {
    name: 'login',
    data() {
      return {
        user: {
          name: '',
          password: ''
        },
        loading: false
      };
    },
    methods: {
      login() {
        this.$router.push({path: '/home'});
        this.loading = true;
        let regex = /[a-zA-Z0-9]/g;
        let regexName = regex.test(this.user.name);
        let regexPwd = regex.test(this.user.password);
        let url = '';
        let data = {user_name: this.user.name, password: this.user.password};
        data = JSON.stringify(data);
        if (this.user.name !== '' && regexName && this.user.password !== '' && regexPwd) {
          api.post(url, data).then(res => {
             this.loading = false;
          });
        } else if (!regexName) {
          this.$message('请输入用户名');
        } else if (!regexPwd) {
          this.$message('请输入密码');
        } else {
          this.$message('用户名和密码不能为空');
        }
      }
    }
  };
</script>

<style scoped lang="scss">
  .container-fluid {
    height: 100vh;
    background-color: rgb(27, 49, 93);
    position: absolute;
    width: 100vw;
    .text-center {
      margin-top: 100px;
      font-size: 30px;
      font-weight: bolder;
    }
  }

  .login {
    width: 380px;
    height: 270px;
    margin: 20px auto;
    background: #fff;
    border-radius: 5px;
    .el-button--text {
      color: #ffffff;
    }
    .el-button {
      font-size: 16px !important;
      font-weight: bolder;
    }
    .form-horizontal .control-label {
      color: rgb(27, 49, 93) !important;
    }
    p {
      background: #32A0FF;
      height: 40px;
      font-weight: bolder;
      line-height: 40px;
      text-align: center;
      color: #ffffff;
      padding: 0 20px;
      border-radius: 5px 5px 0 0;
      font-size: 16px;
      letter-spacing: 10px;
      span {
        float: right;
        font-size: 12px;
      }
    }
    .login-content {
      border-radius: 5px;
      background: #fff;
      width: 100%;
      padding: 15px;
      button {
        float: right;
        margin-top: 20px;
      }
      .btn-link {
        float: right;
        background: none;
        border: none;
        outline: none;
        margin: -8px -10px 0 0;
      }
      .form-group {
        border-bottom: 1px solid #dddddd;
      }
      .form-group:last-child {
        border-bottom: none;
      }
      .form-control {
        border: none;
        box-shadow: none !important;
      }
    }
  }

  .el-dialog__body p {
    text-align: center;
  }

  #label {
    position: relative;
    left: 13.5px;
  }

  .el-button {
    display: block;
    width: 100%;
    font-size: 30px !important;
  }


  .el-input {
    display: block;
    width: 100%;
  }

  .title {
    letter-spacing: 6px;
  }

  .el-button {
    letter-spacing: 10px;
  }

  label {
    letter-spacing: 1px;
  }
</style>
