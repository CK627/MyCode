"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  data() {
    return {
      isLogin: false,
      userInfo: {
        nickname: "",
        avatarUrl: ""
      }
    };
  },
  onLoad() {
    this.checkLoginStatus();
  },
  methods: {
    checkLoginStatus() {
      const token = common_vendor.index.getStorageSync("token");
      if (token) {
        this.isLogin = true;
        const userInfo = common_vendor.index.getStorageSync("userInfo");
        if (userInfo) {
          this.userInfo = JSON.parse(userInfo);
        }
      }
    },
    handleUserInfo(e) {
      if (e.detail.errMsg === "getUserInfo:ok") {
        const userInfo = e.detail.userInfo;
        common_vendor.index.login({
          provider: "weixin",
          success: (loginRes) => {
            this.loginWithCode(loginRes.code, userInfo);
          },
          fail: (err) => {
            common_vendor.index.showToast({
              title: "登录失败",
              icon: "none"
            });
          }
        });
      }
    },
    loginWithCode(code, userInfo) {
      const mockUserInfo = {
        nickname: userInfo.nickName,
        avatarUrl: userInfo.avatarUrl,
        userId: "wx_" + Math.random().toString(36).substr(2, 8)
      };
      common_vendor.index.setStorageSync("token", "mock_token");
      common_vendor.index.setStorageSync("userInfo", JSON.stringify(mockUserInfo));
      this.isLogin = true;
      this.userInfo = mockUserInfo;
      common_vendor.index.showToast({
        title: "登录成功",
        icon: "success"
      });
    }
  }
};
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return common_vendor.e({
    a: $data.userInfo.avatarUrl || "/static/default-avatar.png",
    b: $data.isLogin
  }, $data.isLogin ? {
    c: common_vendor.t($data.userInfo.nickname)
  } : {
    d: common_vendor.o((...args) => $options.handleUserInfo && $options.handleUserInfo(...args))
  });
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render]]);
wx.createPage(MiniProgramPage);
