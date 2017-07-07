<template>
  <el-card>
    <h3 class="text-center">年收入汇总表
      <el-button style='margin-bottom:20px;float:right' type="primary" size="mini" @click="handleDownload">
        <img src="../assets/icon_export.png" alt="">
        导出excel
      </el-button>
    </h3>
    <el-table :data="tableData" style="width: 100%;" border :row-class-name="tableRowClassName" v-loading="loading"
              element-loading-text="拼命加载中">
      <el-table-column label="序号" prop="USER_ID" width="70" align="center"></el-table-column>
      <el-table-column label="部门" prop="OFFICE_ID" width="200" align="center"></el-table-column>
      <el-table-column label="姓名" prop="NAME" width="100" align="center"></el-table-column>
      <el-table-column label="基本工资" align="center">
        <el-table-column label="基本工资" prop="JBGZ" width="100" align="center"></el-table-column>
        <el-table-column label="年限工资" prop="NXGZ" width="100" align="center"></el-table-column>
        <el-table-column label="技术工资" prop="JSGZ" width="100" align="center"></el-table-column>
        <el-table-column label="绩效工资" prop="JXGZ" width="100" align="center"></el-table-column>
        <el-table-column label="技能工资" prop="JNGZ" width="100" align="center"></el-table-column>
      </el-table-column>
      <el-table-column label="加班" align="center">
        <el-table-column label="加班工资" prop="JBGZ" width="100" align="center"></el-table-column>
        <el-table-column label="超时加班费1" prop="CSJBF1" width="150" align="center"></el-table-column>
        <el-table-column label="超时加班费2" prop="CSJBF2" width="150" align="center"></el-table-column>
        <el-table-column label="节日加班费" prop="JRJBF" width="150" align="center"></el-table-column>
      </el-table-column>
      <el-table-column label="补助" align="center">
        <el-table-column label="出勤" prop="CQ" width="100" align="center"></el-table-column>
        <el-table-column label="补助" prop="BZ" width="100" align="center"></el-table-column>
        <el-table-column label="岗位补贴" prop="GWBT" width="100" align="center"></el-table-column>
        <el-table-column label="电话费" prop="DHF" width="100" align="center"></el-table-column>
        <el-table-column label="夜餐费" prop="YCF" width="100" align="center"></el-table-column>
        <el-table-column label="施工补助1" prop="SGBZ" width="110" align="center"></el-table-column>
        <el-table-column label="施工补助2" prop="SGBZ" width="110" align="center"></el-table-column>
        <el-table-column label="公里补助" prop="GLBZ" width="100" align="center"></el-table-column>
        <el-table-column label="交通补助" prop="JTBZ" width="100" align="center"></el-table-column>
        <el-table-column label="慰问补助" prop="WWBZ" width="100" align="center"></el-table-column>
        <el-table-column label="装表采集工程补助" prop="ZBCJGCBZ" width="200" align="center"></el-table-column>
        <el-table-column label="目标管理费" prop="MBGLJ" width="110" align="center"></el-table-column>
        <el-table-column label="带电作业费" prop="DDZYF" width="110" align="center"></el-table-column>
        <el-table-column label="线路巡视维护" prop="LXXSWH" width="130" align="center"></el-table-column>
        <el-table-column label="线路巡视检修费" prop="LXXSJXF" width="150" align="center"></el-table-column>
        <el-table-column label="线路巡视设计费" prop="LXXSSJF" width="150" align="center"></el-table-column>
        <el-table-column label="设备巡视检修费" prop="SBXSJXF" width="150" align="center"></el-table-column>
        <el-table-column label="现场工作负责人安全员岗位补贴" prop="XCGZFZRAQYGWBT" width="300" align="center"></el-table-column>
      </el-table-column>
      <el-table-column label="奖励" align="center">
        <el-table-column label="奖励" prop="JL" align="center" width="100"></el-table-column>
        <el-table-column label="福利" prop="FL" align="center" width="100"></el-table-column>
        <el-table-column label="考核奖" prop="KHJ" align="center" width="100"></el-table-column>
        <el-table-column label="设计考核奖" prop="SJKHJ" align="center" width="120"></el-table-column>
        <el-table-column label="安全优质考核" prop="AQYZKH" align="center" width="130"></el-table-column>
        <el-table-column label="月度考核奖" prop="YDKHJ" align="center" width="120"></el-table-column>
        <el-table-column label="季度考评及季度专项奖" prop="JDKPJJDZXJ" align="center" width="200"></el-table-column>
        <el-table-column label="季度专项奖" prop="JDZXJ" align="center" width="110"></el-table-column>
      </el-table-column>
      <el-table-column label="应发合计" prop="yfhj" width="100"></el-table-column>
      <!--<el-table-column label="扣款" align="center">
        <el-table-column label="扣款" prop="kk" align="center"></el-table-column>
        <el-table-column label="扣税" prop="ks" align="center"></el-table-column>
      </el-table-column>-->
      <el-table-column label="四险一金" prop="center" align="center">
        <el-table-column label="扣养老" prop="JBYLBX1" align="center" width="90"></el-table-column>
        <el-table-column label="扣医保" prop="JBYLBX2" align="center" width="90"></el-table-column>
        <el-table-column label="扣失业" prop="SYBX" align="center" width="90"></el-table-column>
        <el-table-column label="扣公积金" prop="ZFGJJ" width="110" align="center"></el-table-column>
        <el-table-column label="大病救助" prop="DBJZ" width="110" align="center"></el-table-column>
      </el-table-column>
      <el-table-column label="实发工资" prop="TOTAL" width="120" align="center"></el-table-column>
    </el-table>
    <pagination @currentPage="next" :total="total"></pagination>
  </el-card>
</template>
<script>
  import URL from '../api/url';
  import * as api from '../api/api';
  import Pagination from './pagination';
  export default {
    name: 'first',
    components: {
      Pagination
    },
    data() {
      return {
        loading: true,
        tableData: [],
        total: null
      };
    },
    created() {
      this.init();
    },
    methods: {
      tableRowClassName(row, index) {
        if (index % 2 === 1) {
          return 'info-row';
        } else if (index % 2 === 0) {
          return 'positive-row';
        }
        return '';
      },
      init(currentPage = 1) {
        let url = URL.YEAR_SALARY;
        let params = {cur_page: currentPage, page_size: 10};
        api.get(url, params).then(res => {
          this.loading = false;
          window.console.log(res);
          this.tableData = res.data;
          this.total = res.total_num;
        }).catch(err => {
          this.loading = false;
        });
      },
      next(currentPage) {
        this.loading = true;
        this.init(currentPage);
      },
      handleDownload() {
        let year = new Date().getFullYear();
        location.href = `${URL.DOWNLOAD}?year=${year}`;
      }
    }
  };
</script>
<style>
  h3 {
    color: #42d5f6;
    margin-bottom: 20px;
  }

  .el-button {
    margin-top: 25px;
    margin-bottom: 7px !important;
  }

  img {
    width: 12px;
    position: relative;
    top: -2px;
    height: 12px;
  }

  .el-card {
    margin-top: 10px;
    margin-bottom: 20px;
    text-align: center;
  }

  .el-table__header-wrapper {
    color: #fff !important;
    background-color: #20a0ff !important;
  }

  .el-table__header-wrapper .is-leaf {
    color: #fff !important;
    background-color: #20a0ff !important;
  }

  .el-table__header-wrapper .is-leaf div {
    color: #fff !important;
    background-color: #20a0ff !important;
  }

  .el-table__header-wrapper .is-center {
    color: #fff !important;
    background-color: #20a0ff !important;
  }

  .el-table__header-wrapper div {
    color: #fff !important;
    background-color: #20a0ff !important;
  }

  .el-table__header-wrapper div {
    color: #fff !important;
    background-color: #20a0ff !important;
  }

  .el-table {
    margin-top: -10px !important;
  }

  .el-table .info-row {
    background: rgba(32, 160, 255, .2) !important;
  }

  .el-table .positive-row {
    background: #fafafa !important;
  }
</style>
