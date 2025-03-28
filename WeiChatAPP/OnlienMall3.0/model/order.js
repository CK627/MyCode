export const mockFetchOrders = () => {
  return new Promise((resolve) => {
    resolve({
      data: {
        orderList: [], // 清空订单列表
      },
    });
  }); 