<template>
	<view class="content">
		<!-- 个人信息区域 - 添加点击事件 -->
		<navigator url="/pages/userinfo/userinfo" class="profile-section">
			<view class="avatar-wrapper">
				<image class="avatar" :src="userInfo.avatarUrl || '/static/default-avatar.png'" mode="aspectFill"></image>
			</view>
			<view class="user-info" v-if="isLogin">
				<text class="nickname">{{userInfo.nickname}}</text>
			</view>
			<view class="login-btn" v-else>
				<button class="wx-login-btn" open-type="getUserInfo" @getuserinfo="handleUserInfo">微信登录</button>
			</view>
			<text class="arrow">></text>
		</navigator>

		<!-- 订单区域 -->
		<view class="order-section">
			<view class="section-header">
				<text>我的订单</text>
				<navigator url="/pages/orders/orders" class="view-all">
					全部订单
					<text class="arrow">></text>
				</navigator>
			</view>
			<view class="order-types">
				<view class="order-item">
					<text>待付款</text>
				</view>
				<view class="order-item">
					<text>待发货</text>
				</view>
				<view class="order-item">
					<text>待收货</text>
				</view>
				<view class="order-item">
					<text>待评价</text>
				</view>
				<view class="order-item">
					<text>退款/售后</text>
				</view>
			</view>
		</view>

		<!-- 功能列表 -->
		<view class="function-list">
			<navigator url="/pages/address/address" class="function-item">
				<text>收货地址</text>
				<text class="arrow">></text>
			</navigator>
			<navigator url="/pages/service/service" class="function-item">
				<text>客服热线</text>
				<text class="arrow">></text>
			</navigator>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				isLogin: false,
				userInfo: {
					nickname: '',
					avatarUrl: ''
				}
			}
		},
		onLoad() {
			// 检查登录状态
			this.checkLoginStatus()
		},
		methods: {
			checkLoginStatus() {
				const token = uni.getStorageSync('token')
				if (token) {
					this.isLogin = true
					const userInfo = uni.getStorageSync('userInfo')
					if (userInfo) {
						this.userInfo = JSON.parse(userInfo)
					}
				}
			},
			handleUserInfo(e) {
				if (e.detail.errMsg === 'getUserInfo:ok') {
					// 获取用户信息成功
					const userInfo = e.detail.userInfo
					
					// 调用微信登录
					uni.login({
						provider: 'weixin',
						success: (loginRes) => {
							// 获取到code后调用后端接口完成登录
							this.loginWithCode(loginRes.code, userInfo)
						},
						fail: (err) => {
							uni.showToast({
								title: '登录失败',
								icon: 'none'
							})
						}
					})
				}
			},
			loginWithCode(code, userInfo) {
				// 这里需要调用你的后端接口，使用code换取openid等信息
				// 示例代码：
				/*
				uni.request({
					url: 'your-api-url/login',
					method: 'POST',
					data: {
						code: code,
						userInfo: userInfo
					},
					success: (res) => {
						if (res.data.success) {
							// 保存登录信息
							uni.setStorageSync('token', res.data.token)
							uni.setStorageSync('userInfo', JSON.stringify(res.data.userInfo))
							
							this.isLogin = true
							this.userInfo = res.data.userInfo
							
							uni.showToast({
								title: '登录成功',
								icon: 'success'
							})
						}
					},
					fail: (err) => {
						uni.showToast({
							title: '登录失败',
							icon: 'none'
						})
					}
				})
				*/
				
				// 临时演示代码
				const mockUserInfo = {
					nickname: userInfo.nickName,
					avatarUrl: userInfo.avatarUrl,
					userId: 'wx_' + Math.random().toString(36).substr(2, 8)
				}
				uni.setStorageSync('token', 'mock_token')
				uni.setStorageSync('userInfo', JSON.stringify(mockUserInfo))
				
				this.isLogin = true
				this.userInfo = mockUserInfo
				
				uni.showToast({
					title: '登录成功',
					icon: 'success'
				})
			}
		}
	}
</script>

<style>
.content {
	min-height: 100vh;
	background-color: #f5f5f5;
}

.profile-section {
	display: flex;
	align-items: center;
	padding: 30rpx;
	background-color: #ffffff;
}

.avatar-wrapper {
	margin-right: 30rpx;
}

.avatar {
	width: 120rpx;
	height: 120rpx;
	border-radius: 50%;
	background-color: #f5f5f5;
}

.user-info {
	flex: 1;
}

.nickname {
	font-size: 32rpx;
	color: #333;
	font-weight: 500;
}

/* 订单区域样式 */
.order-section {
	margin-top: 20rpx;
	background-color: #fff;
	padding: 20rpx;
}

.section-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 20rpx 0;
	border-bottom: 1rpx solid #eee;
}

.view-all {
	color: #999;
	font-size: 28rpx;
}

.order-types {
	display: flex;
	justify-content: space-between;
	padding: 30rpx 0;
}

.order-item {
	position: relative;
	display: flex;
	flex-direction: column;
	align-items: center;
	flex: 1;
}

.order-item text {
	font-size: 24rpx;
	color: #666;
}

/* 功能列表样式 */
.function-list {
	margin-top: 20rpx;
	background-color: #fff;
}

.function-item {
	display: flex;
	align-items: center;
	padding: 30rpx;
	border-bottom: 1rpx solid #eee;
}

.function-item text:first-child {
	flex: 1;
	font-size: 28rpx;
	color: #333;
}

.arrow {
	color: #999;
	font-size: 28rpx;
}

.wx-login-btn {
	background: #07c160;
	color: #fff;
	font-size: 28rpx;
	border-radius: 40rpx;
	padding: 0 40rpx;
	height: 70rpx;
	line-height: 70rpx;
}

.wx-login-btn::after {
	border: none;
}

.function-item:last-child {
	border-bottom: none;
}
</style> 