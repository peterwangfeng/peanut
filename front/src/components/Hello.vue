<template>
  <el-carousel height="90vh">
    <el-carousel-item label="堆叠柱形图1">
      <highcharts :options="column1"></highcharts>
    </el-carousel-item>
    <el-carousel-item label="堆叠柱形图2">
      <highcharts :options="column2"></highcharts>
    </el-carousel-item>
    <el-carousel-item label="单层环形图">
      <highcharts :options="pie1"></highcharts>
    </el-carousel-item>
    <el-carousel-item label="双层环形图">
      <div class="c-charts">
        <IEcharts :option="pie" style="width: 600px;height: 400px;"></IEcharts>
      </div>
    </el-carousel-item>
    <el-carousel-item label="雷达图">
      <div class="c-charts">
        <IEcharts :option="polar" style="width: 400px;min-height: 400px;"></IEcharts>
      </div>
    </el-carousel-item>
    <el-carousel-item label="仪表盘">
      <div class="c-charts">
        <IEcharts :option="echart" style="width: 600px;height: 400px;"></IEcharts>
      </div>
    </el-carousel-item>
    <el-carousel-item label="表格1">
      <el-table :data="tableData1" border style="width: 100%;">
        <el-table-column label="序号" prop="id" width="70" align="center"></el-table-column>
        <el-table-column label="工资明细" align="center">
          <el-table-column label="部门" prop="dep" width="100" align="center"></el-table-column>
          <el-table-column label="姓名" prop="name" width="100" align="center"></el-table-column>
          <el-table-column label="基本工资" align="center">
            <el-table-column label="基本工资" prop="jbgz" width="100" align="center"></el-table-column>
            <el-table-column label="年限工资" prop="nxgz" width="100" align="center"></el-table-column>
            <el-table-column label="考核工资" prop="khgz" width="100" align="center"></el-table-column>
            <el-table-column label="绩效工资" prop="jxgz" width="100" align="center"></el-table-column>
            <el-table-column label="技能工资" prop="jngz" width="100" align="center"></el-table-column>
          </el-table-column>
          <el-table-column label="加班" align="center">
            <el-table-column label="春节加班" prop="cjjb" width="100" align="center"></el-table-column>
          </el-table-column>
          <el-table-column label="补助" align="center">
            <el-table-column label="通讯补贴" prop="txbt" width="100" align="center"></el-table-column>
            <el-table-column label="夜餐费" prop="ycf" width="100" align="center"></el-table-column>
            <el-table-column label="午餐费" prop="wcf" width="100" align="center"></el-table-column>
            <el-table-column label="公里补贴" prop="glbt" width="100" align="center"></el-table-column>
          </el-table-column>
          <el-table-column label="奖励" align="center">
            <el-table-column label="开门红" prop="jl" align="center" width="100"></el-table-column>
          </el-table-column>
          <el-table-column label="应发合计" prop="yfhj" width="100"></el-table-column>
          <el-table-column label="扣款" align="center">
            <el-table-column label="扣款" prop="kk" align="center"></el-table-column>
            <el-table-column label="扣税" prop="ks" align="center"></el-table-column>
          </el-table-column>
          <el-table-column label="四险一金" prop="center" align="center">
            <el-table-column label="扣养老" prop="yl" align="center" width="90"></el-table-column>
            <el-table-column label="扣医保" prop="yb" align="center" width="90"></el-table-column>
            <el-table-column label="扣失业" prop="ky" align="center" width="90"></el-table-column>
            <el-table-column label="扣公积金" prop="gjj" width="110" align="center"></el-table-column>
          </el-table-column>
          <el-table-column label="实发工资" prop="sfgz" width="120" align="center"></el-table-column>
          <el-table-column label="备注" prop="bz" align="center"></el-table-column>
        </el-table-column>
      </el-table>
    </el-carousel-item>
    <el-carousel-item label="表格2">
      <table class="table table-striped table-hover table-consended" border style="width: 90vw">
        <caption class="text-center h3">各部门工资表</caption>
        <tr>
          <th>季度</th>
          <th>月份</th>
          <th>IT部门</th>
          <th>技术部</th>
          <th>财务部</th>
          <th>人事部</th>
          <th>销售部</th>
          <th>运营部</th>
          <th>总计(月份)</th>
          <th>总计(季度)</th>
        </tr>
        <tr v-for="item in tableData2">
          <td rowspan="3" v-if="item.season">{{item.season}}</td>
          <td>{{item.month}}</td>
          <td>{{item.it}}</td>
          <td>{{item.js}}</td>
          <td>{{item.cw}}</td>
          <td>{{item.rs}}</td>
          <td>{{item.xs}}</td>
          <td>{{item.yy}}</td>
          <td>{{item.zjyf}}</td>
          <td rowspan="3" v-if="item.zjjd">{{item.zjjd}}</td>
        </tr>
      </table>
    </el-carousel-item>
  </el-carousel>
</template>

<script>
  import IEcharts from 'vue-echarts-v3';
  export default {
    name: 'hello',
    components: {
      IEcharts
    },
    data () {
      return {
        column1: {
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
            categories: ['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'],
          },
          credits: {
            enabled: false
          },
          yAxis: {
            plotLines: [{
              width: 1,
              color: '#218080'
            }]
          },
          tooltip: {
            valueSuffix: 'k'
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
            name: '第四季度',
            data: [10000, 20000, 30000, 30000, 20000, 10000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#84dee9'
          }, {
            name: '第三季度',
            data: [10000, 20000, 10000, 20000, 10000, 20000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#34c5d8'
          }, {
            name: '第二季度',
            data: [20000, 10000, 20000, 10000, 20000, 10000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#1bacbf'
          }, {
            name: '第一季度',
            data: [10000, 10000, 20000, 20000, 10000, 10000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#12828e'
          }]
        },
        column2: {
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
            categories: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
          },
          credits: {
            enabled: false
          },
          yAxis: {
            plotLines: [{
              width: 1,
              color: '#218080'
            }]
          },
          tooltip: {
            valueSuffix: 'k',
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
            name: 'IT部门',
            data: [10000, 20000, 30000, 30000, 20000, 10000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#84dee9'
          }, {
            name: '技术部',
            data: [10000, 20000, 10000, 20000, 10000, 20000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#34c5d8'
          }, {
            name: '销售部',
            data: [20000, 10000, 20000, 10000, 20000, 10000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#1bacbf'
          }, {
            name: '财务部',
            data: [10000, 10000, 20000, 20000, 10000, 10000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#12828e'
          }, {
            name: '人事部',
            data: [10000, 20000, 20000, 20000, 10000, 10000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: 'orange'
          }, {
            name: '运营部',
            data: [10000, 20000, 100000, 20000, 10000, 10000, 10000, 20000, 30000, 30000, 20000, 10000],
            color: '#a9ff96'
          }]
        },
        pie1: {
          chart: {
            plotBackgroundColor: null,
            plotBorderWidth: 0,
            plotShadow: false,
          },
          title: {
            text: '¥100.000',
            align: 'center',
            verticalAlign: 'middle',
          },
          credits: {
            enabled: false
          },
          tooltip: {
            headerFormat: '{series.name}<br>',
            pointFormat: '{point.name}: <b>{point.percentage:.1f}%</b>'
          },
          plotOptions: {
            pie: {
              dataLabels: {
                enabled: true,
                distance: -50,
                style: {
                  fontWeight: 'bold',
                  color: 'white',
                  textShadow: '0px 1px 2px black'
                }
              },
              center: ['50%', '50%']
            }
          },
          series: [
            {
              type: 'pie',
              name: '绩效工资季度占比',
              innerSize: '70%',
              data: [
                ['第一季度', 26],
                ['第二季度', 23],
                ['第三季度', 37],
                ['第四季度', 14],
              ]
            }
          ]
        },
        pie2: {
          chart: {
            polar: true,
            backgroundColor: 'rgb(13,30,70)'
          },
          title: {
            text: '分类工资分布情况',
            x: -80
          },
          pane: {
            size: '80%'
          },
          xAxis: {
            categories: ['基本工资', '四险一金', '补助', '加班', '福利', '奖励'],
            tickmarkPlacement: 'on',
            lineWidth: 0
          },
          yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            min: 0
          },
          tooltip: {
            shared: true,
            pointFormat: '<span style="color:{series.color}">{series.name}: <b>${point.y:,.0f}</b><br/>'
          },
          legend: {
            align: 'right',
            verticalAlign: 'top',
            y: 70,
            layout: 'vertical'
          },
          series: [
            {
              name: '1',
              data: [40000, 5000, 10000, 1000, 500, 500],
              pointPlacement: 'on'
            },
            {
              name: '2',
              data: [140000, 5000, 10000, 1000, 500, 500],
              pointPlacement: 'on'
            }
          ]
        },
        polar: {
          title: {
//            text: '',
          },
          tooltip: {},
          legend: {
            itemGap: 20,
            textStyle: {
              color: '#000',
              fontSize: 14
            },
            data: ['预算工资', '实际工资'],
//            selectedMode: 'single'
          },
          radar: {
//            shape: 'circle',
            indicator: [
              {name: '基本工资'},
              {name: '四险一金'},
              {name: '补助'},
              {name: '加班'},
              {name: '福利'},
              {name: '奖励'},
            ]
          },
          series: [{
            type: 'radar',
            areaStyle: {normal: {}},
            data: [
              {
                itemStyle: {normal: {color: 'rgb(87, 188, 218)'}},
                value: [4300, 10000, 28000, 35000, 50000, 19000],
                name: '预算工资',
                label: {
                  normal: {
                    show: true,
                    formatter: function (params) {
                      return params.value;
                    }
                  }
                }
              },
              {
                itemStyle: {normal: {color: 'rgb(13, 66, 97)'}},
                value: [5000, 14000, 28000, 31000, 42000, 21000],
                name: '实际工资',
                label: {
                  normal: {
                    show: true,
                    formatter(params) {
                      return params.value;
                    }
                  }
                }
              }
            ]
          }]
        },
        pie: {
          tooltip: {
            trigger: 'item',
            formatter: "{a} <br/>{b}: {c} ({d}%)"
          },
          legend: {
            orient: 'vertical',
            x: 'left',
            data: ['第一季度', '第二季度', '第三季度', '第四季度']
          },
          series: [
            {
              name: '',
              type: 'pie',
//              selectedMode: 'single',
              radius: ['70%', '50%'],
              label: {
                normal: {
                  position: 'inner'
                }
              },
              labelLine: {
                normal: {
                  show: false
                }
              },
              data: [
                {value: 335, name: '第一季度', itemStyle: {normal: {color: 'rgb(0,120,131)'}}},
                {value: 679, name: '第二季度', itemStyle: {normal: {color: 'rgb(0,162,185)'}}},
                {value: 1548, name: '第三季度', itemStyle: {normal: {color: 'rgb(34,190,212)'}}},
                {value: 1548, name: '第四季度', itemStyle: {normal: {color: 'rgb(117,217,232)'}}}
              ]
            },
            {
              name: '',
              type: 'pie',
              radius: ['70%', '90%'],
              data: [
                {value: 335, name: '第一季度', itemStyle: {normal: {color: 'rgb(0,120,131)'}}},
                {value: 310, name: '第二季度', itemStyle: {normal: {color: '#ec7777'}}},
                {value: 234, name: '第三季度', itemStyle: {normal: {color: '#e5c649'}}},
                {value: 135, name: '第四季度', itemStyle: {normal: {color: '#a6c733'}}},
              ]
            }
          ]
        },
        gauge: {

          chart: {
            type: 'gauge',
            plotBackgroundColor: null,
            plotBackgroundImage: null,
            plotBorderWidth: 0,
            plotShadow: false
          },

          title: {
            text: 'Speedometer'
          },

          pane: {
            startAngle: -150,
            endAngle: 150,
            background: [{
              backgroundColor: {
                linearGradient: {x1: 0, y1: 0, x2: 0, y2: 1},
                stops: [
                  [0, '#FFF'],
                  [1, '#333']
                ]
              },
              borderWidth: 0,
              outerRadius: '109%'
            }, {
              backgroundColor: {
                linearGradient: {x1: 0, y1: 0, x2: 0, y2: 1},
                stops: [
                  [0, '#333'],
                  [1, '#FFF']
                ]
              },
              borderWidth: 1,
              outerRadius: '107%'
            }, {
              // default background
            }, {
              backgroundColor: '#DDD',
              borderWidth: 0,
              outerRadius: '105%',
              innerRadius: '103%'
            }]
          },

          // the value axis
          yAxis: {
            min: 0,
            max: 200,

            minorTickInterval: 'auto',
            minorTickWidth: 1,
            minorTickLength: 10,
            minorTickPosition: 'inside',
            minorTickColor: '#666',

            tickPixelInterval: 30,
            tickWidth: 2,
            tickPosition: 'inside',
            tickLength: 10,
            tickColor: '#666',
            labels: {
              step: 2,
              rotation: 'auto'
            },
            title: {
              text: 'km/h'
            },
            plotBands: [{
              from: 0,
              to: 120,
              color: '#55BF3B' // green
            }, {
              from: 120,
              to: 160,
              color: '#DDDF0D' // yellow
            }, {
              from: 160,
              to: 200,
              color: '#DF5353' // red
            }]
          },

          series: [{
            name: 'Speed',
            data: [80],
            tooltip: {
              valueSuffix: ' km/h'
            }
          }]
        },
        echart: {
          title: {
            x: "center",
            top: 10,

          },
          tooltip: {
            formatter: "{a} <br/>{b} : {c}%"
          },
          series: [{
            name: '绩效工资季度',
            type: 'gauge',
            // startAngle: 180,
            // endAngle: 0,
            min: 0,
            max: 100000,
            axisLine: {
              show: true,
              lineStyle: {
                width: 30,
                shadowBlur: 0,
                color: [[0.3, '#E43F3D'], [0.6, '#E98E2C'], [0.8, '#DDBD4D'], [1, '#7CBB55']]
              }
            },
            axisTick: {
              show: true,
              splitNumber: 1
            },
            splitLine: {
              show: false,
            },
            axisLabel: {
              /*  formatter: function (e) {
               switch (e + "") {
               case "410":
               return "第一季度";
               case "530":
               return "第二季度";
               case "650":
               return "第三季度";
               case "770":
               return "第四季度";
               default:
               return '';
               }
               },*/
              textStyle: {
                fontSize: 15,
                fontWeight: ""
              }
            },
            pointer: {
              show: false,
            },
            detail: {
              formatter: '{value}',
              offsetCenter: [0, -10],
              textStyle: {
                fontSize: 50
              }
            },
            data: [{
              name: "第二季度",
              value: 4.6
            }]
          }]
        },
        tableData1: [
          {
            id: 1,
            dep: '技术部',
            name: '张三',
            jbgz: 3000,
            nxgz: 200,
            khgz: 500,
            jxgz: 1000,
            jngz: 300,
            cjjb: null,
            txbt: 100,
            ycf: 100,
            wcf: 200,
            glbt: 100,
            jl: 200,
            yfhj: 5900,
            kk: '',
            ks: 200,
            yl: 50,
            yb: 50,
            ky: 50,
            gjj: 50,
            sfgz: 5500,
            bz: null
          },
          {
            id: 2,
            dep: '事务部',
            name: '王五',
            jbgz: 3000,
            nxgz: 200,
            khgz: 500,
            jxgz: 1000,
            jngz: 300,
            cjjb: null,
            txbt: 100,
            ycf: 100,
            wcf: 200,
            glbt: 100,
            jl: 200,
            yfhj: 5900,
            kk: '',
            ks: 200,
            yl: 50,
            yb: 50,
            ky: 50,
            gjj: 50,
            sfgz: 5500,
            bz: null
          },
          {
            id: 3,
            dep: '市场部',
            name: '李四',
            jbgz: 3000,
            nxgz: 200,
            khgz: 500,
            jxgz: 1000,
            jngz: 300,
            cjjb: null,
            txbt: 100,
            ycf: 100,
            wcf: 200,
            glbt: 100,
            jl: 200,
            yfhj: 5900,
            kk: '',
            ks: 200,
            yl: 50,
            yb: 50,
            ky: 50,
            gjj: 50,
            sfgz: 5500,
            bz: null
          },
          {
            id: 4,
            dep: '后勤部',
            name: '曹尼玛',
            jbgz: 3000,
            nxgz: 200,
            khgz: 500,
            jxgz: 1000,
            jngz: 300,
            cjjb: null,
            txbt: 100,
            ycf: 100,
            wcf: 200,
            glbt: 100,
            jl: 200,
            yfhj: 5900,
            kk: '',
            ks: 200,
            yl: 50,
            yb: 50,
            ky: 50,
            gjj: 50,
            sfgz: 5500,
            bz: null
          },
          {
            id: '5',
            dep: '工程部',
            name: '赵六',
            jbgz: 3000,
            nxgz: 200,
            khgz: 500,
            jxgz: 1000,
            jngz: 300,
            cjjb: null,
            txbt: 100,
            ycf: 100,
            wcf: 200,
            glbt: 100,
            jl: 200,
            yfhj: 5900,
            kk: '',
            ks: 200,
            yl: 50,
            yb: 50,
            ky: 50,
            gjj: 50,
            sfgz: 5500,
            bz: null
          }
        ],
        tableData2: [
          {
            season: '第一季度',
            month: '一月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895,
            zjjd: 45690
          },
          {
            month: '二月',
            it: 4000,
            js: 2000,
            cw: 310,
            rs: 2310,
            xs: 4900,
            yy: 3400,
            zjyf: 16920
          },
          {
            month: '三月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895
          },
          {
            season: '第二季度',
            month: '四月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895,
            zjjd: 45690
          },
          {
            month: '五月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895
          },
          {
            month: '六月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895
          },
          {
            season: '第三季度',
            month: '七月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895,
            zjjd: 45600
          },
          {
            month: '八月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895
          },
          {
            month: '九月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895
          },
          {
            season: '第四季度',
            month: '十月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895,
            zjjd: 45690
          },
          {
            month: '十一月',
            it: 2500,
            js: 5000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895
          },
          {
            month: '十二月',
            it: 8000,
            js: 6000,
            cw: 2000,
            rs: 1995,
            xs: 2200,
            yy: 3200,
            zjyf: 16895
          }
        ]
      };
    },
  };
</script>

<style scoped>
  .c-charts {
    height: 500px;
    width: 500px;
    margin: 0 auto;
  }

  table {
    border: 1px solid #000;
    border-collapse: collapse;
    margin: 0 auto;
  }

  th {
    text-align: center;
    background-color: rgba(0, 172, 196, .7);
  }

  tr:nth-of-type(1) {
    font-size: 16px;
    height: 50px;
    color: #fff;
    font-weight: bold;
  }

  th, td {
    height: 30px;
  }

  tr:nth-of-type(2n) {
    background-color: #ecfafb;
  }

  tr:nth-of-type(2n+1) {
    background-color: #fafafa;
  }
</style>
