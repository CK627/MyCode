<template>
	<view class="userinfo-container">
		<view class="info-item" @click="chooseAvatar">
			<text class="label">头像</text>
			<view class="value-wrapper">
				<image class="avatar" :src="userInfo.avatarUrl || '/static/default-avatar.png'" mode="aspectFill"></image>
				<text class="arrow">></text>
			</view>
		</view>
		
		<view class="info-item" @click="editNickname">
			<text class="label">昵称</text>
			<view class="value-wrapper">
				<text class="value">{{userInfo.nickname || '未设置'}}</text>
				<text class="arrow">></text>
			</view>
		</view>
		
		<view class="info-item" @click="editGender">
			<text class="label">性别</text>
			<view class="value-wrapper">
				<text class="value">{{genderText}}</text>
				<text class="arrow">></text>
			</view>
		</view>
		
		<view class="info-item" @click="bindPhone">
			<text class="label">手机号</text>
			<view class="value-wrapper">
				<text class="value">{{userInfo.phone || '未绑定'}}</text>
				<text class="arrow">></text>
			</view>
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			userInfo: {
				nickname: '',
				avatarUrl: '',
				gender: 0, // 0-未设置 1-男 2-女
				phone: ''
			}
		}
	},
	computed: {
		genderText() {
			const genderMap = {
				0: '未设置',
				1: '男',
				2: '女'
			}
			return genderMap[this.userInfo.gender]
		}
	},
	onLoad() {
		const userInfo = uni.getStorageSync('userInfo')
		if (userInfo) {
			this.userInfo = JSON.parse(userInfo)
		}
	},
	methods: {
		chooseAvatar() {
			uni.chooseImage({
				count: 1,
				sizeType: ['compressed'],
				sourceType: ['album', 'camera'],
				success: (res) => {
					// 这里应该先上传图片到服务器，获取URL后再更新
					this.userInfo.avatarUrl = res.tempFilePaths[0]
					this.updateUserInfo()
				}
			})
		},
		editNickname() {
			uni.navigateTo({
				url: '/pages/userinfo/nickname'
			})
		},
		editGender() {
			uni.showActionSheet({
				itemList: ['男', '女'],
				success: (res) => {
					this.userInfo.gender = res.tapIndex + 1
					this.updateUserInfo()
				}
			})
		},
		bindPhone() {
			// 调用微信手机号授权
			uni.showModal({
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
			uni.setStorageSync('userInfo', JSON.stringify(this.userInfo))
			uni.showToast({
				title: '更新成功',
				icon: 'success'
			})
		}
	}
}
</script>

<style>
.userinfo-container {
	background-color: #f5f5f5;
	min-height: 100vh;
}

.info-item {
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding: 30rpx;
	background-color: #fff;
	border-bottom: 1rpx solid #eee;
}

.label {
	font-size: 28rpx;
	color: #333;
}

.value-wrapper {
	display: flex;
	align-items: center;
}

.value {
	font-size: 28rpx;
	color: #666;
	margin-right: 10rpx;
}

.avatar {
	width: 80rpx;
	height: 80rpx;
	border-radius: 50%;
	margin-right: 10rpx;
}

.arrow {
	color: #999;
	font-size: 28rpx;
}
</style> 