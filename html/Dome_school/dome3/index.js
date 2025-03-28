document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('registerForm');
    
    form.addEventListener('submit', (e) => {
        e.preventDefault();
        
        // 密码长度验证
        const password = document.getElementById('password').value;
        if(password.length < 6 || password.length > 16) {
            alert('密码长度需在6-16位之间');
            return;
        }
        
        // 身份证格式验证
        const idNumber = document.getElementById('idNumber').value;
        const idPattern = /^\d{17}[\dXx]$/;
        if(!idPattern.test(idNumber)) {
            alert('请输入有效的18位身份证号码');
            return;
        }
        
        // 邮箱格式验证
        const email = document.getElementById('email').value;
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if(!emailPattern.test(email)) {
            alert('请输入有效的电子邮箱');
            return;
        }
        
        // 提交表单数据
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());
        console.log('提交数据：', data);
        alert('注册信息已提交！');
    });

    // 重置按钮事件
    form.addEventListener('reset', () => {
        document.querySelectorAll('.form-group input, select, textarea').forEach(element => {
            element.value = '';
        });
    });
});