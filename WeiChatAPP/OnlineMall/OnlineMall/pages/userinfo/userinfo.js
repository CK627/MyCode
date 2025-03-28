Page({
	data: {
		userInfo: {
			nickname: '',
			avatarUrl: '',
			gender: 0, // 0-未设置 1-男 2-女
			phone: ''
		}
	},

	onLoad() {
		const userInfo = wx.getStorageSync('userInfo')
		if (userInfo) {
			this.setData({
				userInfo: JSON.parse(userInfo)
			})
		}
	},

	// 计算性别显示文本
	getGenderText(gender) {
		const genderMap = {
			0: '未设置',
			1: '男',
			2: '女'
		}
		return genderMap[gender]
	},

	chooseAvatar() {
		wx.chooseImage({
			count: 1,
			sizeType: ['compressed'],
			sourceType: ['album', 'camera'],
			success: (res) => {
				// 这里应该先上传图片到服务器，获取URL后再更新
				this.setData({
					'userInfo.avatarUrl': res.tempFilePaths[0]
				})
				this.updateUserInfo()
			}
		})
	},

	editNickname() {
		wx.navigateTo({
			url: '/pages/userinfo/nickname'
		})
	},

	editGender() {
		wx.showActionSheet({
			itemList: ['男', '女'],
			success: (res) => {
				this.setData({
					'userInfo.gender': res.tapIndex + 1
				})
				this.updateUserInfo()
			}
		})
	},

	bindPhone() {
		wx.showModal({
			title: '提示',
			content: '是否使用微信手机号快速绑定？',
			success: (res) => {
				if (res.confirm) {
					// 获取微信手机号的逻辑
				}
			}
		})
	},

	updateUserInfo() {
		// 这里应该调用后端接口更新用户信息
		wx.setStorageSync('userInfo', JSON.stringify(this.data.userInfo))
		wx.showToast({
			title: '更新成功',
			icon: 'success'
		})
	}
}) 