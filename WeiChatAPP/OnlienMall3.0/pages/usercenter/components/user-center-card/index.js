const AuthStepType = {
  ONE: 1,
  TWO: 2,
  THREE: 3,
};

Component({
  options: {
    multipleSlots: true,
  },
  properties: {
    currAuthStep: {
      type: Number,
      value: AuthStepType.ONE,
    },
    userInfo: {
      type: Object,
      value: {},
    },
    isNeedGetUserInfo: {
      type: Boolean,
      value: false,
    },
  },
  data: {
    defaultAvatarUrl: 'https://cdn-we-retail.ym.tencent.com/miniapp/usercenter/icon-user-center-avatar@2x.png',
    AuthStepType,
  },
  methods: {
    onGetUserInfo(e) {
      if (e.detail.userInfo) {
        const userInfo = e.detail.userInfo;
        this.setData({
          'userInfo.avatarUrl': userInfo.avatarUrl,
          'userInfo.nickName': userInfo.nickName,
          currAuthStep: 2,
        });
        this.triggerEvent('updateUserInfo', { userInfo });
      }
    },
    gotoUserEditPage() {
      this.triggerEvent('gotoUserEditPage');
    },
  },
});
