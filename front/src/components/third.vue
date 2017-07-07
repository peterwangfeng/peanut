<template>
  <el-card>
    <div class="charts">
      <h3 class="text-center">公司各部门工资分布情况报表</h3>
      <el-row>
        <el-button @click="change">{{click}}</el-button>
        <!--<el-button :type="type==='month'?'primary':''" @click="type='month'">按月</el-button>-->
        <el-date-picker
          v-model="date"
          :type="type"
          align="left"
          placeholder="选择日期">
        </el-date-picker>
        <el-select v-model="option" placeholder="请选择">
          <el-option v-for="option in options" :key="option.label" :label="option.label"
                     :value="option.value"></el-option>
        </el-select>
        <el-button type="primary" @click="init">确定</el-button>
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
        click: '按年',
        type: 'month',
        date: new Date(),
        option: '5ee2506d6b584e70a4267ba0e893aec3',
        options: [
          {label: '营销部', value: '5ee2506d6b584e70a4267ba0e893aec3'},
          {label: '抄收用电服务部', value: '1c3df6a9f2654e65a0876ced537e9add'},
          {label: '安全运检部', value: 'b5d1800d8a77463cac04522c8dac692a'},
          {label: '电力调度中心', value: '5917ff2cc86f4033aa8ee9a46c7dff80'},
          {label: '发展建设部', value: '81cfe6feb056455ea75fbfe3309c4075'},
          {label: '档案室', value: 'b798b037ff5a4c9da2aea546f143d9fc'},
          {label: '输电工程分公司', value: '1a0bb9f3916f4aa596b082c7fc2e1c83'},
          {label: '物业分公司', value: 'e272604e0df940fba8a6a5421089df3f'},
          {label: '设计分公司', value: 'd943566e6def4da485ef2fadc3788ac4'},
          {label: '输配电运维分公司', value: '38f51528044f459c891013c30e6600c0'},
          {label: '仪征恒邦实业有限公司', value: 'b144c48ac3bb4fb881be54e99331e85f'},
          {label: '生产单位', value: 'cf4c2c36b55441a7b7cacd80582b82e5'},
          {label: '管理部门', value: '89db7c73ef494ad782dee55c9645f07b'},
          {label: '事务部', value: '766fa018013d41ec96995de1010c5f7c'},
          {label: '财务部', value: 'c05e6ef18704442e80ac134eb0635235'},
          {label: '市场部', value: '1b5527cdae1d4c419e9170ef61c5e9bf'},
          {label: '工程部', value: 'ebb83e7cddb24b11912f7448b6467f48'},
          {label: '综合服务分公司', value: '188110fa13d14f5287d42bbaeb5c1d70'},
          {label: '器材分公司', value: 'b82410d91f6742a1b4250cc906073baf'},
          {label: '电力工程服务分公司', value: '709002de2d4342c79c32ee916fe3ba63'},
          {label: '输配电工程分公司', value: '0207d05722e8431d91c1e21bdfb9da54'},
          {label: '变电工程分公司', value: '5d080393140a48368409159d03de5eff'},
          {label: '城南用电服务部', value: '6bb1c7d4a1bf4e78b3104e92a2437ed7'},
          {label: '公司领导', value: 'f7873c0c3e6d4209becc49f5f1137e7e'},
        ],
        polar: {
          title: {},
          tooltip: {},
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
    },
    methods: {
      change() {
        if (this.type === 'month') {
          this.type = 'year';
          this.click = '按月'
        } else {
          this.type = 'month';
          this.click = '按年';
        }
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
    text-align: center !important;
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
