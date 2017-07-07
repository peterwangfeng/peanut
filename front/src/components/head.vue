<template>
  <div class="header">
    <el-col :span="12" style="text-align: left;padding-left: 30px;font-size: 20px;font-weight: bold">
      <span>绩效工资分析系统</span>
    </el-col>
    <el-col :span="12" style="text-align: right;padding-right: 10px">
      <el-tooltip effect="dark" :content="name" placement="bottom">
        <a href="javascript:void(0)" style="height: 58px;color: #fff;text-decoration: none;position: relative;left:-5px;">
          <i class="fa fa-user" style="font-size: 24px;color: #fff;position: relative;top:4px;left:-10px;"></i>
          {{name}}
        </a>
      </el-tooltip>
      &nbsp;&nbsp;
      <el-tooltip effect="dark" content="退出" placement="bottom">
        <a href="javascript:void(0)" style="height: 58px;" @click="logout">
          <i class="fa fa-sign-out" style="font-size: 24px;position: relative;top: 4px;left:-13px;color: #fff;"></i>
        </a>
      </el-tooltip>
    </el-col>
  </div>
</template>

<script>
  import URL from '../api/url';
  import * as api from '../api/api';
  export default {
    name: 'heads',
    data() {
      return {
        name: null,
        user_id: null
      };
    },
    created() {
      this.name = window.localStorage.getItem('name') || '管理员';
      this.user_id = window.localStorage.getItem('user_id');
    },
    methods: {
      logout() {
        this.$confirm('你确定退出吗?', '温馨提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          let url = URL.LOGOUT;
          let data = {user_id: this.user_id};
          data = JSON.stringify(data);
          api.post(url, data).then(res => {
            window.sessionStorage.clear();
            window.localStorage.clear();
            this.$router.push({name: 'login'});
          });
        });
      }
    }
  };
</script>

<style lang="scss" scoped>
  .header {
    height: 50px;
    width: 100%;
    position: fixed;
    z-index: 2000;
    line-height: 50px;
    background-color: rgba(11, 27, 67, .9) !important;
    color: #fff;
  }
</style>

