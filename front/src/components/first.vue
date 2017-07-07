<template>
  <div class="contain">
    <el-card>
      <h3 class="text-center">公司年度费用预算支出分析报表</h3>
      <div style="width: 600px;height: 400px;" id="pie"></div>
    </el-card>
    <el-card>
      <h3 class="text-center">近10年的绩效工资支出分布报表</h3>
      <highcharts :options="column"></highcharts>
    </el-card>
  </div>
</template>
<script>
  import URL from '../api/url';
  import * as api from '../api/api';
  import echarts from 'echarts';
  export default {
    name: 'first',
    data() {
      return {
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
              text: '年份',
            }
          },
          credits: {
            enabled: false
          },
          yAxis: {
            title: {
              text: '工资(万元)'
            },
            plotLines: [{
              width: 1,
              color: '#218080'
            }]
          },
          tooltip: {
            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.percentage:.0f}%)<br/>',
            shared: true,
            valueSuffix: '万元',
            backgroundColor: 'rgba(255,255,255,.98)'
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
            color: '#84dee9'
          }, {
            name: '',
            data: [],
            color: '#34c5d8'
          }, {
            name: '',
            data: [],
            color: '#1bacbf'
          }, {
            name: '',
            data: [],
            color: '#12828e'
          }]
        },
        pie: {
          angleAxis: {
            axisLine: {
              show: true,
              type: 'dotted'
            },
            axisPointer: {
              show: true,
              type: 'shadow',
              label: {
                show: true
              }
            }
          },
          tooltip: {
            show: true,
            trigger: 'item',
            valueSuffix: '万元'
          },
          radiusAxis: {
            type: 'category',
            data: [],
            splitNumber: 2,
            z: 10,
          },
          polar: {},
          series: [{
            type: 'bar',
            barWidth: 50,
            data: [],
            itemStyle: {normal: {color: '#9fe6ed'}},
            coordinateSystem: 'polar',
            name: '第一季度',
            stack: 'a'
          }, {
            type: 'bar',
            data: [],
            barWidth: 50,
            itemStyle: {normal: {color: '#56d3de'}},
            coordinateSystem: 'polar',
            name: '第二季度',
            stack: 'a'
          }, {
            type: 'bar',
            barWidth: 50,
            data: [],
            itemStyle: {normal: {color: '#3bbdcb'}},
            coordinateSystem: 'polar',
            name: '第三季度',
            stack: 'a'
          }, {
            type: 'bar',
            barWidth: 50,
            data: [],
            itemStyle: {normal: {color: '#2a99a1'}},
            coordinateSystem: 'polar',
            name: '第四季度',
            stack: 'a'
          }],
          legend: {
            show: true,
            data: ['第一季度', '第二季度', '第三季度', '第四季度']
          }
        }
      };
    },
    created() {
      this.init();
    },
    mounted() {
      this.$nextTick(function () {
        this.initPie();
      })
    },
    methods: {
      init() {
        let url = URL.JD_SALARY;
        let params = {years: '2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022'};
        api.get(url, params).then(res => {
          window.console.log(res);
          this.column.xAxis.categories = res.category.years;
          for (let i = 0; i < res.category.seasons.length; i++) {
            this.column.series[i].name = res.category.seasons[i];
          }
          for (let i = 0; i < res.series.length; i++) {
            this.column.series[i].data = res.series[i];
          }
        });
      },
      initPie() {
        let myChart = echarts.init(document.getElementById('pie'));
        let url = URL.JD_SALARY;
        let year = new Date().getFullYear();
        let params = {years: year};
        api.get(url, params).then(res => {
          this.pie.radiusAxis.data = res.category;
          for (let i = 0; i < res.series.length; i++) {
            this.pie.series[i].data = res.series[i];
          }
          myChart.setOption(this.pie);
        });
      }
    }
  };
</script>
<style scoped>
  .contain {
    height: 400px;
  }

  h3 {
    color: #42d5f6;
    margin-bottom: 30px;
  }

  #pie {
    margin: 0 auto;
  }

  .el-card {
    margin-top: 10px;
    margin-bottom: 10px;
    transition: all .3s linear;
    border-radius: 8px;
  }
</style>
