<template>
  <div class="container-fluid">
    <div class="header">
      <heads></heads>
    </div>
    <div class="sidebar">
      <sidebar></sidebar>
    </div>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import Heads from './head';
  import Sidebar from './sidebar';
  export default {
    name: 'home',
    components: {
      Heads,
      Sidebar
    }
  };
</script>

<style lang="scss" scoped>
  .container-fluid {
    padding-right: 0 !important;
    padding-left: 0 !important;
  }

  .header {
    background: #324257;
  }

  .sidebar {
    width: 80px;
  }

  .content {
    margin-top: 50px;
    padding: 20px 25px 0 195px;
    color: #000;
  }
</style>
