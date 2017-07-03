<template>
  <div class="header">
    <el-col span="12" style="text-align: left;padding-left: 30px;font-size: 20px;font-weight: bold">
      <span>绩效工资分析系统</span>
    </el-col>
    <el-col span="12" style="text-align: right;padding-right: 10px">
      <el-tooltip effect="dark" content="退出" placement="bottom">
        <a href="javascript:void(0)" style="height: 58px;" @click="logout">
          <i class="fa fa-sign-out" style="font-size: 24px;position: relative;top: -0.5px;color: #fff;"></i>
        </a>
      </el-tooltip>
    </el-col>
  </div>
</template>

<script>
  export default {
    name: 'heads',
    methods: {
      logout() {
        this.$router.push({path: '/'});
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
    background-color: #324157 !important;
    color: #fff;
  }
</style>

