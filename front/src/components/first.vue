<template>
  <div class="contain">
    <el-card>
      <h3 class="text-center">公司年度费用预算支出分析报表</h3>
      <el-row>
        <el-date-picker v-model="value" align="right" type="year" @change="handle" placeholder="选择年份">
        </el-date-picker>
      </el-row>
      <!--<div style="width: 600px;height: 400px;" id="pie"></div>-->
      <el-row>
        <IEcharts style="width: 600px;min-height: 400px;" :option="polar" v-loading="loading" element-loading-text="拼命加载中,请稍后..."></IEcharts>
      </el-row>
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
import IEcharts from 'vue-echarts-v3';
export default {
  name: 'first',
  components: {
    IEcharts
  },
  data() {
    return {
      loading: true,
      value: new Date(),
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
          itemStyle: { normal: { color: '#9fe6ed' } },
          coordinateSystem: 'polar',
          name: '第一季度',
          stack: 'a'
        }, {
          type: 'bar',
          data: [],
          barWidth: 50,
          itemStyle: { normal: { color: '#56d3de' } },
          coordinateSystem: 'polar',
          name: '第二季度',
          stack: 'a'
        }, {
          type: 'bar',
          barWidth: 50,
          data: [],
          itemStyle: { normal: { color: '#3bbdcb' } },
          coordinateSystem: 'polar',
          name: '第三季度',
          stack: 'a'
        }, {
          type: 'bar',
          barWidth: 50,
          data: [],
          itemStyle: { normal: { color: '#2a99a1' } },
          coordinateSystem: 'polar',
          name: '第四季度',
          stack: 'a'
        }],
        legend: {
          show: true,
          data: ['第一季度', '第二季度', '第三季度', '第四季度']
        }
      },
      polar: {
        tooltip: {
          formatter: "{a}<br/>已使用 {c} {b}"
        },
        series: [
          {
            name: '全年',
            type: 'gauge',
            z: 5,
            min: 0,
            max: 300,
            splitNumber: 10,
            radius: '70%',
            axisLine: {            // 坐标轴线
              lineStyle: {       // 属性lineStyle控制线条样式
                width: 10,
                color: [[0.1, '#91c7ae'], [0.667, '#63869e'], [1, '#c23531']]
              }
            },
            axisTick: {            // 坐标轴小标记
              length: 15,        // 属性length控制线长
              lineStyle: {       // 属性lineStyle控制线条样式
                color: 'auto'
              }
            },
            splitLine: {           // 分隔线
              length: 20,         // 属性length控制线长
              lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
                color: 'auto'
              }
            },
            title: {
              textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: 'bolder',
                fontSize: 20,
                fontStyle: 'italic'
              }
            },
            detail: {
              textStyle: {       // 其余属性默认使用全局文本样式，详见TEXTSTYLE
                fontWeight: 'bolder'
              }
            },
            data: [{ value: 0, name: '万元' }]
          },
          {
            name: '第一季度',
            type: 'gauge',
            center: ['15%', '50%'],    // 默认全局居中
            radius: '40%',
            min: 0,
            max: 2,
            startAngle: 150,
            endAngle: 30,
            splitNumber: 2,
            axisLine: {            // 坐标轴线
              lineStyle: {       // 属性lineStyle控制线条样式
                width: 8,
                color: [[0.1, '#91c7ae'], [0.667, '#63869e'], [1, '#c23531']]
              }
            },
            axisTick: {            // 坐标轴小标记
              splitNumber: 5,
              length: 10,        // 属性length控制线长
              lineStyle: {       // 属性lineStyle控制线条样式
                width: 8,
                color: 'auto'
              }
            },
            axisLabel: {
              formatter: function (v) {
              }
            },
            splitLine: {           // 分隔线
              length: 15,         // 属性length控制线长
              lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
                color: 'auto'
              }
            },
            pointer: {
              width: 2
            },
            title: {
              show: false
            },
            detail: {
              show: false
            },
            data: [{ value: 0, name: '万元' }]
          },
          {
            name: '第二季度',
            type: 'gauge',
            center: ['85%', '50%'],    // 默认全局居中
            radius: '40%',
            min: 0,
            max: 2,
            startAngle: 150,
            endAngle: 30,
            splitNumber: 2,
            axisLine: {            // 坐标轴线
              lineStyle: {       // 属性lineStyle控制线条样式
                width: 8,
                color: [[0.1, '#91c7ae'], [0.667, '#63869e'], [1, '#c23531']]
              }
            },
            axisTick: {            // 坐标轴小标记
              splitNumber: 5,
              length: 10,        // 属性length控制线长
              lineStyle: {       // 属性lineStyle控制线条样式
                color: 'auto'
              }
            },
            axisLabel: {
              formatter: function (v) {
              }
            },
            splitLine: {           // 分隔线
              length: 15,         // 属性length控制线长
              lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
                color: 'auto'
              }
            },
            pointer: {
              width: 2
            },
            title: {
              show: false
            },
            detail: {
              show: false
            },
            data: [{ value: 0, name: '万元' }]
          },
          {
            name: '第三季度',
            type: 'gauge',
            center: ['15%', '50%'],    // 默认全局居中
            radius: '40%',
            min: 0,
            max: 2,
            startAngle: 330,
            endAngle: 210,
            splitNumber: 2,
            axisLine: {            // 坐标轴线
              lineStyle: {       // 属性lineStyle控制线条样式
                width: 8,
                color: [[0.1, '#91c7ae'], [0.667, '#63869e'], [1, '#c23531']]
              }
            },
            axisTick: {            // 坐标轴小标记
              show: false
            },
            axisLabel: {
              formatter: function (v) {
                /* switch (v + '') {
                 case '0' :
                 return '0';
                 case '1' :
                 return '第三季度';
                 case '2' :
                 return '20';
                 }*/
              }
            },
            splitLine: {           // 分隔线
              length: 15,         // 属性length控制线长
              lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
                color: 'auto'
              }
            },
            pointer: {
              width: 2
            },
            title: {
              show: false
            },
            detail: {
              show: false
            },
            data: [{ value: 0, name: '万元' }]
          },
          {
            name: '第四季度',
            type: 'gauge',
            center: ['85%', '50%'],    // 默认全局居中
            radius: '40%',
            min: 0,
            max: 2,
            startAngle: 330,
            endAngle: 210,
            splitNumber: 2,
            axisLine: {            // 坐标轴线
              lineStyle: {       // 属性lineStyle控制线条样式
                width: 8,
                color: [[0.1, '#91c7ae'], [0.667, '#63869e'], [1, '#c23531']]
              }
            },
            axisTick: {            // 坐标轴小标记
              show: false
            },
            axisLabel: {
              formatter: function (v) {

              }
            },
            splitLine: {           // 分隔线
              length: 15,         // 属性length控制线长
              lineStyle: {       // 属性lineStyle（详见lineStyle）控制线条样式
                color: 'auto'
              }
            },
            pointer: {
              width: 2
            },
            title: {
              show: false
            },
            detail: {
              show: false
            },
            data: [{ value: 0, name: '万元' }]
          }
        ]
      }
    };
  },
  created() {
    this.init();
    this.initPie();
  },
  methods: {
    handle() {
      this.loading = true;
      this.initPie();
    },
    init() {
      let url = URL.JD_SALARY;
      let params = { years: '2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022' };
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
      let url = URL.JD_SALARY;
      let year = this.value.getFullYear();
      let params = { years: year };
      let self = this;
      api.get(url, params).then(res => {
        this.loading = false;
        let sea = ['第一季度', '第二季度', '第三季度', '第四季度'];
        let all =  ['全年','第一季度', '第二季度', '第三季度', '第四季度'];
        for (let i = 0; i < res.series.length; i++) {
          let max = res.series[i][0] > res.series[i][1] ? res.series[i][0] : res.series[i][1];
          if (max === 0) {
            max = 100;
          }
          this.polar.series[i].max = Number.parseInt(max) * 1.5;
          if (i !== 0) {
            self.polar.series[i].splitNumber = 4;
            self.polar.series[i].axisLabel.formatter = (v) => {
              switch (v + '') {
                case '0':
                  return '0';
                case this.polar.series[i].max / 2 + '':
                  return sea[i - 1];
                case this.polar.series[i].max + '':
                  return self.polar.series[i].max;
              }
            };
          }
          this.polar.series[i].axisLine.lineStyle.color[1][0] = Number((res.series[i][1] / this.polar.series[i].max).toFixed(3));
          this.polar.series[i].data[0].value = res.series[i][0];
          this.polar.series[i].name = all[i] + '(预算' + res.series[i][1] + '万元)';
        }
      });
    }
  }
};
</script>
<style scoped>
.contain {
  height: 400px;
}

.el-row {
  text-align: right;
  margin-bottom: 20px;
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
  border-radius: 10px;
}

.vue-echarts {
  margin: 10px auto;
}
</style>
