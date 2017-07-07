<template>
  <div>
    <el-card>
      <h3>公司各部门经费支出情况报表</h3>
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
            color: '#9fe6ed'
          }, {
            name: '',
            data: [],
            color: '#56d3de'
          }, {
            name: '',
            data: [],
            color: '#3bbdcb'
          }, {
            name: '',
            data: [],
            color: '#2a99a1'
          }, {
            name: '',
            data: [],
            color: '#3d6f4e'
          }, {
            name: '',
            data: [],
            color: '#4c944c'
          }, {
            name: '',
            data: [],
            color: '#c1d87a'
          }, {
            name: '',
            data: [],
            color: '#e7ecab'
          }, {
            name: '',
            data: [],
            color: '#a4d4bf'
          }, {
            name: '',
            data: [],
            color: '#89c79b'
          }, {
            name: '',
            data: [],
            color: '#47a48a'
          }, {
            name: '',
            data: [],
            color: '#3ab291'
          }, {
            name: '',
            data: [],
            color: '#2a99a1'
          }, {
            name: '',
            data: [],
            color: '#3bbdcb'
          }, {
            name: '',
            data: [],
            color: '#56d3de'
          }, {
            name: '',
            data: [],
            color: '#9fe6ed'
          }, {
            name: '',
            data: [],
            color: '#2a99a1'
          }, {
            name: '',
            data: [],
            color: '#9fe6ed'
          }, {
            name: '',
            data: [],
            color: '#56d3de'
          }, {
            name: '',
            data: [],
            color: '#3bbdcb'
          }, {
            name: '',
            data: [],
            color: '#2a99a1'
          }, {
            name: '',
            data: [],
            color: '#3d6f4e'
          }, {
            name: '',
            data: [],
            color: '#4c944c'
          }, {
            name: '',
            data: [],
            color: '#c1db7a'
          }]
        }
      };
    },
    created() {
      this.init();
    },
    methods: {
      init() {
        let url = URL.DEPART_MONTH;
        api.getWithNoParams(url).then(res => {
          this.loading = false;
          this.tableData = res;
        });
        let year = new Date().getFullYear();
        let params = {year: year, months: '01,02,03,04,05,06,07,08,09,10,11,12'};
        api.get(url, params).then(res => {
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
    border-radius: 8px;
    margin-bottom: 10px;
    min-height: 100px;
  }

  .el-table {
    margin-top: 10px !important;
    margin-bottom: 20px;
  }

</style>
