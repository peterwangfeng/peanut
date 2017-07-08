<template>
  <el-card>
    <div class="charts">
      <h3 class="text-center">公司各部门工资分布情况报表</h3>
      <el-row>
        <el-button :type="type==='year'?'primary':''" @click="handleType('year')">按年</el-button>
        <el-button :type="type==='month'?'primary':''" @click="handleType('month')">按月</el-button>
        <el-date-picker
          v-model="date"
          :type="type"
          align="left"
          @change="handle"
          :clearable="false"
          placeholder="选择日期">
        </el-date-picker>
        <el-select v-model="option" placeholder="请选择" @change="handle" style="position: relative;top: 1px;">
          <el-option v-for="option in options" :key="option.NAME" :label="option.NAME"
                     :value="option.ID"></el-option>
        </el-select>
        <!--<el-button type="primary" @click="init">确定</el-button>-->
      </el-row>
      <IEcharts :option="polar" style="width: 600px;min-height: 600px;" v-loading="loading"
                element-loading-text="拼命加载中,请稍后..."></IEcharts>
    </div>
  </el-card>
</template>
<script>
  import IEcharts from 'vue-echarts-v3';
  import * as api from '../api/api';
  import URL from '../api/url';
  export default {
    name: 'third',
    components: {
      IEcharts
    },
    data() {
      return {
        loading: true,
        type: 'month',
        date: new Date(),
        option: '5ee2506d6b584e70a4267ba0e893aec3',
        options: [],
        polar: {
          title: {},
          tooltip: {
            backgrounlogdColor: '#fff',
            color: '#000'
          },
          legend: {
            itemGap: 20,
            textStyle: {
              color: '#000',
              fontSize: 14
            },
          },
          radar: {
            indicator: [
              {text: '基本工资'},
              {text: '补助'},
              {text: '加班'},
              {text: '奖励'},
              {text: '四险一金'},
            ]
          },
          series: [{
            type: 'radar',
            areaStyle: {normal: {}},
            tooltip: {
              trigger: 'item'
            },
            data: [
              {
                itemStyle: {normal: {color: 'rgb(87, 188, 218)'}},
                value: [],
                name: '营销部',
                label: {
                  normal: {
                    show: true,
                    formatter: function (params) {
                      return params.value;
                    }
                  }
                }
              }]
          }]
        }
      };
    },
    created() {
      this.init();
      let url = URL.GET_DEPART;
      api.getWithNoParams(url).then(res => {
        this.options = res;
      });
    },
    methods: {
      /*change() {
       if (this.type === 'month') {
       this.type = 'year';
       this.click = '按月'
       } else {
       this.type = 'month';
       this.click = '按年';
       }
       },*/
      handle(value) {
        console.log(value);
        this.init();
      },
      handleType(value) {
        this.type = value;
        this.init();
      },
      init() {
        let url = URL.DEPART_CATEGARY;
        if (this.type === 'month') {
          let year = this.date.getFullYear();
          let mon = this.date.getMonth() + 1;
          mon = mon < 10 ? `0${mon}` : mon;
          let params = {year: year, month: mon, depart: this.option};
          api.get(url, params).then(res => {
            this.loading = false;
            this.polar.radar.indicator = res.category;
            this.polar.series[0].data[0].value = res.series;
            this.polar.series[0].data[0].name = res.depart_name;
          }).catch(err => {
            this.loading = false;
          });
        } else if (this.type === 'year') {
          let year = this.date.getFullYear();
          let params = {year: year, depart: this.option};
          api.get(url, params).then(res => {
            this.loading = false;
            this.polar.radar.indicator = res.category;
            this.polar.series[0].data[0].value = res.series;
            this.polar.series[0].data[0].name = res.depart_name;
          }).catch(err => {
            this.loading = false;
          });
        }
      }
    }
  };
</script>
<style scoped>
  .el-row {
    text-align: right !important;
  }

  .charts {
    width: 100%;
    margin: 0 auto;
    text-align: center;
  }

  .el-row {
    text-align: center;
  }

  .vue-echarts {
    margin: 10px auto;
  }

  h3 {
    color: #42d5f6;
    margin-bottom: 30px;
  }

  .vue-echarts {
    text-align: center;
  }

  .el-card {
    margin-top: 10px;
    height: 680px !important;
    margin-bottom: 20px;
    transition: all .3s linear;
  }
</style>
