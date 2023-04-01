<template></template>

<script>
export default {
  data() {
    return {
      // Collapse navigation value.
      // Binded model property for "Collapsible Navigation Menu" collapsed status .
      collapseNav: 0,
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
      openKeys: null,
    };
  },
  methods: {
    onOpenChange(openKeys) {
      this.openKeys = this.openKeys
        ? this.openKeys
        : this.$route.meta.sidebarMap;

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

<style lang="scss" scoped>
.nav-link svg {
  margin-right: 5px;
  vertical-align: middle;
}
.nav-link span {
  vertical-align: middle;
}
.ant-menu-submenu-popup {
  width: 100%;
}
</style>