"use strict";
const common_vendor = require("../../common/vendor.js");
const _sfc_main = {
  data() {
    return {
      userInfo: {
        nickname: "",
        avatarUrl: "",
        gender: 0,
        // 0-未设置 1-男 2-女
        phone: ""
      }
    };
  },
  computed: {
    genderText() {
      const genderMap = {
        0: "未设置",
        1: "男",
        2: "女"
      };
      return genderMap[this.userInfo.gender];
    }
  },
  onLoad() {
    const userInfo = common_vendor.index.getStorageSync("userInfo");
    if (userInfo) {
      this.userInfo = JSON.parse(userInfo);
    }
  },
  methods: {
    chooseAvatar() {
      common_vendor.index.chooseImage({
        count: 1,
        sizeType: ["compressed"],
        sourceType: ["album", "camera"],
        success: (res) => {
          this.userInfo.avatarUrl = res.tempFilePaths[0];
          this.updateUserInfo();
        }
      });
    },
    editNickname() {
      common_vendor.index.navigateTo({
        url: "/pages/userinfo/nickname"
      });
    },
    editGender() {
      common_vendor.index.showActionSheet({
        itemList: ["男", "女"],
        success: (res) => {
          this.userInfo.gender = res.tapIndex + 1;
          this.updateUserInfo();
        }
      });
    },
    bindPhone() {
      common_vendor.index.showModal({
        title: "提示",
        content: "是否使用微信手机号快速绑定？",
        success: (res) => {
          if (res.confirm)
            ;
        }
      });
    },
    updateUserInfo() {
      common_vendor.index.setStorageSync("userInfo", JSON.stringify(this.userInfo));
      common_vendor.index.showToast({
        title: "更新成功",
        icon: "success"
      });
    }
  }
};
function _sfc_render(_ctx, _cache, $props, $setup, $data, $options) {
  return {
    a: $data.userInfo.avatarUrl || "/static/default-avatar.png",
    b: common_vendor.o((...args) => $options.chooseAvatar && $options.chooseAvatar(...args)),
    c: common_vendor.t($data.userInfo.nickname || "未设置"),
    d: common_vendor.o((...args) => $options.editNickname && $options.editNickname(...args)),
    e: common_vendor.t($options.genderText),
    f: common_vendor.o((...args) => $options.editGender && $options.editGender(...args)),
    g: common_vendor.t($data.userInfo.phone || "未绑定"),
    h: common_vendor.o((...args) => $options.bindPhone && $options.bindPhone(...args))
  };
}
const MiniProgramPage = /* @__PURE__ */ common_vendor._export_sfc(_sfc_main, [["render", _sfc_render]]);
wx.createPage(MiniProgramPage);
