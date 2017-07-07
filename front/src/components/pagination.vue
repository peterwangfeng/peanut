<template>
  <div class="pagination">
    <el-pagination @current-change="handleCurrentChange" :current-page.sync="countCurrentpage"
                   :page-size="pagination.pageSize" layout="total, prev, pager, next" :total="total">
    </el-pagination>
  </div>
</template>

<script>
  export default {
    props: {
      total: {
        type: Number,
        default: 1,
        validator: function (value) {
          return value >= 0;
        }
      },
      currentP: {
        type: Number,
        default: 1
      }
    },
    data() {
      return {
        pagination: {
          pageSize: 10
        }
      };
    },
    computed: {
      countCurrentpage() {
          return this.currentP;
      }
    },
    created() {
      this.pagination.total = this.total;
    },
    methods: {
      handleCurrentChange(val) {
        this.pagination.currentPage = val;
        this.getCurrentChange(val);
      },
      getCurrentChange(currentPage) {
        this.$emit('currentPage', currentPage);
      }
    }
  };
</script>

<style lang="scss" scoped>
  .pagination {
    display: table;
    vertical-align: middle;
    margin: 20px auto 0;
  }
</style>
