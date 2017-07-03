<template>
  <el-row class="tac">
    <el-col :span="8">
      <el-menu :default-active="$route.path" class="el-menu-vertical-demo" theme="dark" unique-opened router>
        <el-menu-item index="/home/first">
          <span class="icon">
            <span>绩效预算控制分析</span>
          </span>
        </el-menu-item>
        <el-menu-item index="/home/second">
          <span class="icon">
            <span>部门工资分布情况</span>
          </span>
        </el-menu-item>
        <el-menu-item index="/home/third">
          <span class="icon">
            <span>分类工资分布情况</span>
          </span>
        </el-menu-item>
        <el-menu-item index="/home/fourth">
          <span class="icon">
            <span>年收入汇总</span>
          </span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'sidebar',
    data() {
      return {
      };
    }
  };
</script>

<style scoped lang="scss">
  .el-col-8 {
    width: 220px !important;
    position: fixed !important;
    bottom: 0 !important;
    top: 50px !important;
    height: calc(100% - 50px) !important;
    background-color: #324157 !important;
    overflow-y: auto;
    z-index: 9998;
    .el-menu {
      > .el-menu-item {
        border-top: 1px solid #475669;
      }
      .el-submenu {
        border-top: 1px solid #475669;
        .el-menu-item {
          height: 40px !important;
          line-height: 40px !important;
          margin-top: -15px;
        }
      }
      .el-submenu:last-child {
        border-bottom: 1px solid #475669;
      }
    }
  }
</style>
