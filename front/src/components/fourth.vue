<template>
  <table class="table table-striped table-bordered table-hover">
    <tr>
      <th>月份</th>
      <th>IT部门</th>
      <th>技术部</th>
      <th>财务部</th>
      <th>人事部</th>
      <th>销售部</th>
      <th>运营部</th>
      <th>总计</th>
    </tr>
    <tr v-for="(value, key) in tableData">
      <td>{{key}}</td>
      <td>{{}}</td>
    </tr>
  </table>
</template>
<script>
  import url from '../api/url';
  import * as api from '../api/api';
  export default {
    name: 'fourth',
    data() {
      return {
        tableData: null
      };
    },
    created() {
    },
    methods: {
      initData() {
        let url = '';
        api.get(url).then(res => {
          this.tableData = res;
        });
      }
    }
  };
</script>
<style scoped>
  table {
    border: 1px solid #ccc;
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
