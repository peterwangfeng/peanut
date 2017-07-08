<template>
  <el-row class="tac">
    <el-col :span="8">
      <el-menu :default-active="$route.path" class="el-menu-vertical-demo" theme="dark" unique-opened router>
        <el-menu-item index="/home/first">
          <span class="icon">
            <span><img src="../assets/icon_ys1.png" alt="">&nbsp;&nbsp;绩效预算</span>
          </span>
        </el-menu-item>
        <el-menu-item index="/home/second">
          <span class="icon">
            <span><img src="../assets/icon_bm1.png" alt="">&nbsp;&nbsp;部门工资</span>
          </span>
        </el-menu-item>
        <el-menu-item index="/home/third">
          <span class="icon">
            <span><img src="../assets/icon_fl1.png.png" alt="">&nbsp;&nbsp;工资分类</span>
          </span>
        </el-menu-item>
        <el-menu-item index="/home/fourth">
          <span class="icon">
            <span><img src="../assets/icon_nian1.png" alt="">&nbsp;&nbsp;收入明细</span>
          </span>
        </el-menu-item>
      </el-menu>
    </el-col>
  </el-row>
</template>

<script>
  export default {
    name: 'sidebar'
  };
</script>

<style scoped lang="scss">
  .el-col-8 {
    width: 170px !important;
    position: fixed !important;
    background-color: rgb(11, 27, 67) !important;
    bottom: 0 !important;
    top: 50px !important;
    height: calc(100% - 50px) !important;
    overflow-y: auto;
    z-index: 9998;

    .el-menu {
      background-color: rgb(11, 27, 67) !important;
      font-size: 40px !important;

      >
      .el-menu-item {
        border: none !important;
        text-align: left !important;
      }
      .el-menu-item:hover {
        background-color: rgba(0, 0, 0, .3) !important;
      }
      .el-submenu {
        border-top: 1px solid #475669;

        .el-menu-item {
          text-align: left !important;
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

  img {
    width: 20px;
    height: 20px;
    position: relative;
    top: -1px;
    border-radius: 50%;
  }
</style>
