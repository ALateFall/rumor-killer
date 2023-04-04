<template>
  <!-- Main Sidebar -->
  <a-layout-sider
    collapsible
    class="sider-primary"
    breakpoint="lg"
    collapsed-width="0"
    width="250px"
    :collapsed="sidebarCollapsed"
    @collapse="$emit('toggleSidebar', !sidebarCollapsed)"
    :trigger="null"
    :class="[
      'ant-layout-sider-' + sidebarColor,
      'ant-layout-sider-' + sidebarTheme,
    ]"
    theme="light"
    :style="{ backgroundColor: 'transparent' }"
  >
    <div class="brand">
      <img src="images/logo-ct-black.png" alt="" />
      <span style="font-size:20px;">Rumor Killer</span>
    </div>
    <hr />

    <!-- Sidebar Navigation Menu -->
    <a-menu
      theme="light"
      mode="inline"
      :open-keys="openKeys"
      @openChange="onOpenChange"
    >
      <a-menu-item>
        <router-link to="/index">
          <span class="icon">
            <svg
              width="20"
              height="20"
              viewBox="0 0 20 20"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M3 4C3 3.44772 3.44772 3 4 3H16C16.5523 3 17 3.44772 17 4V6C17 6.55228 16.5523 7 16 7H4C3.44772 7 3 6.55228 3 6V4Z"
                fill="#111827"
              />
              <path
                d="M3 10C3 9.44771 3.44772 9 4 9H10C10.5523 9 11 9.44771 11 10V16C11 16.5523 10.5523 17 10 17H4C3.44772 17 3 16.5523 3 16V10Z"
                fill="#111827"
              />
              <path
                d="M14 9C13.4477 9 13 9.44771 13 10V16C13 16.5523 13.4477 17 14 17H16C16.5523 17 17 16.5523 17 16V10C17 9.44771 16.5523 9 16 9H14Z"
                fill="#111827"
              />
            </svg>
          </span>
          <span class="label">热门话题检测</span>
        </router-link>
      </a-menu-item>

      <!-- <a-sub-menu key="data_get" style="padding: 0">
        <span slot="title">
          <span class="icon">
            <a-icon type="dashboard" theme="filled" class="m-0" />
          </span>
          <span class="label">数据采集引擎</span>
        </span>
        <a-menu-item-group>
          <a-menu-item>
            <router-link to="/eventhandler">
              <span class="label">采集任务概览</span>
            </router-link>
          </a-menu-item>
          <a-menu-item>
            <router-link to="/taskstatus">
              <span class="label">任务处理状态</span>
            </router-link>
          </a-menu-item>
        </a-menu-item-group>
      </a-sub-menu>

      <a-sub-menu key="data_analyze" style="padding: 0">
        <span slot="title">
          <span class="icon">
            <a-icon type="dashboard" theme="filled" class="m-0" />
          </span>
          <span class="label">数据分析结果</span>
        </span>
        <a-menu-item-group>
          <a-menu-item>
            <router-link to="/eventresult">
              <span class="label">数据分析概览</span>
            </router-link>
          </a-menu-item>
          <a-menu-item>
            <router-link to="/websiteresult">
              <span class="label">网站分析结果</span>
            </router-link>
          </a-menu-item>
        </a-menu-item-group>
      </a-sub-menu>

      <a-menu-item>
        <router-link to="/AIQA">
          <span class="icon">
            <svg
              width="20"
              height="20"
              viewBox="0 0 20 20"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M3 4C3 3.44772 3.44772 3 4 3H16C16.5523 3 17 3.44772 17 4V6C17 6.55228 16.5523 7 16 7H4C3.44772 7 3 6.55228 3 6V4Z"
                fill="#111827"
              />
              <path
                d="M3 10C3 9.44771 3.44772 9 4 9H10C10.5523 9 11 9.44771 11 10V16C11 16.5523 10.5523 17 10 17H4C3.44772 17 3 16.5523 3 16V10Z"
                fill="#111827"
              />
              <path
                d="M14 9C13.4477 9 13 9.44771 13 10V16C13 16.5523 13.4477 17 14 17H16C16.5523 17 17 16.5523 17 16V10C17 9.44771 16.5523 9 16 9H14Z"
                fill="#111827"
              />
            </svg>
          </span>
          <span class="label">智能问答系统</span>
        </router-link>
      </a-menu-item>

      <a-sub-menu key="data_find" style="padding: 0">
        <span slot="title">
          <span class="icon">
            <a-icon type="dashboard" theme="filled" class="m-0" />
          </span>
          <span class="label">溯源查证系统</span>
        </span>
        <a-menu-item-group>
          <a-menu-item>
            <router-link to="/websitetrace">
              <span class="label">网站追踪溯源</span>
            </router-link>
          </a-menu-item>
          <a-menu-item>
            <router-link to="/websiteevidence">
              <span class="label">网站查证系统</span>
            </router-link>
          </a-menu-item>
        </a-menu-item-group>
      </a-sub-menu>

      <a-menu-item>
        <router-link to="/usermanage">
          <span class="icon">
            <svg
              width="20"
              height="20"
              viewBox="0 0 20 20"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M3 4C3 3.44772 3.44772 3 4 3H16C16.5523 3 17 3.44772 17 4V6C17 6.55228 16.5523 7 16 7H4C3.44772 7 3 6.55228 3 6V4Z"
                fill="#111827"
              />
              <path
                d="M3 10C3 9.44771 3.44772 9 4 9H10C10.5523 9 11 9.44771 11 10V16C11 16.5523 10.5523 17 10 17H4C3.44772 17 3 16.5523 3 16V10Z"
                fill="#111827"
              />
              <path
                d="M14 9C13.4477 9 13 9.44771 13 10V16C13 16.5523 13.4477 17 14 17H16C16.5523 17 17 16.5523 17 16V10C17 9.44771 16.5523 9 16 9H14Z"
                fill="#111827"
              />
            </svg>
          </span>
          <span class="label">用户权限管理</span>
        </router-link>
      </a-menu-item> -->
    </a-menu>
    <!-- / Sidebar Navigation Menu -->

    <!-- Sidebar Footer -->
    <div class="aside-footer">
      <div class="footer-box">
        <span class="icon">
          <svg
            width="20"
            height="20"
            viewBox="0 0 20 20"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              d="M3 4C3 3.44772 3.44772 3 4 3H16C16.5523 3 17 3.44772 17 4V6C17 6.55228 16.5523 7 16 7H4C3.44772 7 3 6.55228 3 6V4Z"
              fill="#111827"
            />
            <path
              d="M3 10C3 9.44771 3.44772 9 4 9H10C10.5523 9 11 9.44771 11 10V16C11 16.5523 10.5523 17 10 17H4C3.44772 17 3 16.5523 3 16V10Z"
              fill="#111827"
            />
            <path
              d="M14 9C13.4477 9 13 9.44771 13 10V16C13 16.5523 13.4477 17 14 17H16C16.5523 17 17 16.5523 17 16V10C17 9.44771 16.5523 9 16 9H14Z"
              fill="#111827"
            />
          </svg>
        </span>
        <h6>任何疑问?</h6>
        <p>请联系管理人员获取帮助</p>
        <a-button
          block
          size="small"
          href="https://demos.creative-tim.com/muse-vue-ant-design-dashboard-pro/documentation/overview"
          target="_blank"
        >
          <a-icon type="mail" style="font-size:20px;" />
          <span style="font-size:16px;font-weight:bold;">邮件联系</span>
        </a-button>
      </div>
    </div>
    <!-- / Sidebar Footer -->
  </a-layout-sider>
  <!-- / Main Sidebar -->
</template>

<script>
export default {
  props: {
    // Sidebar collapsed status.
    sidebarCollapsed: {
      type: Boolean,
      default: false,
    },

    // Main sidebar color.
    sidebarColor: {
      type: String,
      default: "primary",
    },

    // Main sidebar theme : light, white, dark.
    sidebarTheme: {
      type: String,
      default: "light",
    },
  },
  data() {
    return {
      rootSubmenuKeys: [
        "dashboards",
        "pages",
        "applications",
        "ecommerce",
        "authentication",
        "basic",
        "components",
        "changelog",
      ],
      openKeys: this.$route.meta.sidebarMap,
    };
  },
  methods: {
    onOpenChange(openKeys) {
      const latestOpenKey = openKeys.find(
        (key) => this.openKeys.indexOf(key) === -1
      );

      if (this.rootSubmenuKeys.indexOf(latestOpenKey) === -1) {
        this.openKeys = openKeys;
      } else {
        this.openKeys = latestOpenKey ? [latestOpenKey] : [];
      }
    },
  },
};
</script>
