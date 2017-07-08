<template>
  <div>
    <el-card>
      <h3>公司各部门经费支出情况报表</h3>
      <div class="text-right" style="text-align: right !important;">
        <el-date-picker
          v-model="value"
          align="right"
          type="year"
          @change="handle"
          placeholder="选择年">
        </el-date-picker>
      </div>
      <highcharts :options="column" v-loading="loading1" element-loading-text="拼命加载中,请稍后..."></highcharts>
    </el-card>
    <el-card>
      <h3>公司各部门经费支出情况表格</h3>
      <el-table :data="tableData" border style="width: 100%" v-loading="loading" element-loading-text="拼命加载中...">
        <el-table-column prop="MONTH" label="月份" align="center" width="150"></el-table-column>
        <el-table-column prop="AQYJB" label="安全运检部" align="center" width="120px"></el-table-column>
        <el-table-column prop="BDGCFGS" label="变电工程分公司" align="center" width="150px"></el-table-column>
        <el-table-column prop="CSYDFWB" label="抄收用电服务部" align="center" width="150px"></el-table-column>
        <el-table-column prop="DAS" label="档案室" align="center"></el-table-column>
        <el-table-column prop="DLDDZX" label="电力调度中心" align="center" width="130px"></el-table-column>
        <el-table-column prop="FZJSB" label="发展建设部" align="center" width="120px"></el-table-column>
        <el-table-column prop="GCB" label="工程部" align="center"></el-table-column>
        <el-table-column prop="QCFGS" label="器材分公司" align="center" width="120px"></el-table-column>
        <el-table-column prop="SDGCFGS" label="输电工程分公司" align="center" width="150px"></el-table-column>
        <el-table-column prop="SJFGS" label="设计分公司" align="center" width="120px"></el-table-column>
        <el-table-column prop="SPDGCFGS" label="输配电工程分公司" align="center" width="160px"></el-table-column>
        <el-table-column prop="SPDYWFGS" label="输配电运维分公司" align="center" width="160px"></el-table-column>
        <el-table-column prop="SWB" label="事务部" align="center"></el-table-column>
        <el-table-column prop="YXB" label="营销部" align="center"></el-table-column>
        <el-table-column prop="ZHFWFGS" label="综合服务分公司" align="center" width="150px"></el-table-column>
        <el-table-column prop="GSLD" label="公司领导" align="center" width="100px"></el-table-column>
        <el-table-column prop="CNYDFWB" label="城南用电服务部" align="center" width="150px"></el-table-column>
        <el-table-column prop="DLGCFWFGS" label="电力工程服务分公司" align="center" width="200px"></el-table-column>
        <el-table-column prop="SCB" label="市场部" align="center"></el-table-column>
        <el-table-column prop="CWB" label="财务部" align="center"></el-table-column>
        <el-table-column prop="GLBM" label="管理部门" align="center" width="100px"></el-table-column>
        <el-table-column prop="SCDW" label="生产单位" align="center" width="100px"></el-table-column>
        <el-table-column prop="YZHBSYYXGS" label="仪征恒邦实业有限公司" width="200px" align="center"></el-table-column>
        <el-table-column prop="WYFGS" label="物业分公司" align="center" width="120px"></el-table-column>
        <el-table-column prop="SUM" label="总计" align="center" width="200"></el-table-column>
      </el-table>
    </el-card>
  </div>
</template>
<script>
  import URL from '../api/url';
  import * as api from '../api/api';
  export default {
    name: 'second',
    data() {
      return {
        value: new Date(),
        loading1: true,
        loading: true,
        tableData: [],
        column: {
          chart: {
            type: 'column',
          },
          title: {
            text: '',
            x: -20,
            y: 0
          },
          subtitle: {
            x: -20
          },
          xAxis: {
            categories: [],
            title: {
              text: '月份'
            }
          },
          credits: {
            enabled: false
          },
          yAxis: {
            title: {
              text: '部门工资(万元)'
            },
            plotLines: [{
              width: 1,
              color: '#218080'
            }]
          },
          tooltip: {
            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
            shared: true,
            backgroundColor: 'rgba(255,255,255,.98)',
            valueSuffix: '万元'
          },
          legend: {
            layout: 'horizontal',
            align: 'center',
            verticalAlign: 'top',
            borderWidth: 0
          },
          plotOptions: {
            column: {
              stacking: 'normal',
              pointWidth: 50
            }
          },
          series: [{
            name: '',
            data: [],
            color: '#61bd6d'
          }, {
            name: '',
            data: [],
            color: '#1abc9c'
          }, {
            name: '',
            data: [],
            color: '#54acd2'
          }, {
            name: '',
            data: [],
            color: '#2c82c9'
          }, {
            name: '',
            data: [],
            color: '#9365b8'
          }, {
            name: '',
            data: [],
            color: '#475577'
          }, {
            name: '',
            data: [],
            color: '#41a85f'
          }, {
            name: '',
            data: [],
            color: '#00a885'
          }, {
            name: '',
            data: [],
            color: '#3d8eb9'
          }, {
            name: '',
            data: [],
            color: '#2969b0'
          }, {
            name: '',
            data: [],
            color: '#553982'
          }, {
            name: '',
            data: [],
            color: '#28324e'
          }, {
            name: '',
            data: [],
            color: '#f7da64'
          }, {
            name: '',
            data: [],
            color: '#fba026'
          }, {
            name: '',
            data: [],
            color: '#eb6b56'
          }, {
            name: '',
            data: [],
            color: '#e14938'
          }, {
            name: '',
            data: [],
            color: '#a38f84'
          }, {
            name: '',
            data: [],
            color: '#ef2b33'
          }, {
            name: '',
            data: [],
            color: '#fac51c'
          }, {
            name: '',
            data: [],
            color: '#f37934'
          }, {
            name: '',
            data: [],
            color: '#d14841'
          }, {
            name: '',
            data: [],
            color: '#b8312f'
          }, {
            name: '',
            data: [],
            color: '#75706b'
          }, {
            name: '',
            data: [],
            color: '#853ad8'
          }]
        }
      };
    },
    created() {
      this.init();
    },
    methods: {
      handle() {
        this.loading = true;
        this.init();
      },
      init() {
        let url = URL.DEPART_MONTH;
        let year = this.value.getFullYear();
        let params1 = {year: year};
        api.get(url, params1).then(res => {
          this.loading = false;
          this.tableData = res;
        });
        let params2 = {year: year, months: '01,02,03,04,05,06,07,08,09,10,11,12'};
        api.get(url, params2).then(res => {
          this.loading = false;
          this.column.xAxis.categories = res.category.month;
          for (let i = 0; i < res.category.depart.length; i++) {
            this.column.series[i].name = res.category.depart[i];
          }
          for (let i = 0; i < res.series.length; i++) {
            this.column.series[i].data = res.series[i];
          }
        }).catch(err => {
          this.loading = false;
        });
      }
    }
  };
</script>
<style scoped>
  h3 {
    text-align: center;
    color: #42d5f6;
    margin-bottom: 27px;
  }

  .el-card {
    margin-top: 10px;
    border-radius: 10px !important;
    margin-bottom: 10px;
    min-height: 100px;
  }

  .el-row {
    text-align: right;
  }

  .el-table {
    margin-top: 10px !important;
    margin-bottom: 20px;
  }

</style>
