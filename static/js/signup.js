const inputUserId = document.getElementById('inputId');
const inputPassword = document.getElementById('inputPassword');
const confrimPassword = document.getElementById('confirmPassword');
const inputUserName = document.getElementById('inputName');
const inputYear = document.getElementById('inputYear');
const inputUserNickname = document.getElementById('inputNickname');

inputUserId.addEventListener('keyup', idCheck);
inputPassword.addEventListener('keyup', passwordCheck);
confrimPassword.addEventListener('keyup', isSameCheck);
inputUserName.addEventListener('keyup', nameCheck);
inputYear.addEventListener('keyup', yearCheck);
inputUserNickname.addEventListener('keyup', nicknameCheck);

function NoMultiChk(chk){
    var obj = document.getElementsByName("overlap");
    for(var i=0; i<obj.length; i++){
    if(obj[i] != chk){
        obj[i].checked = false;
    }
    }
}

function idCheck() {
    let userIdLength = inputUserId.value.length;
    if (userIdLength >= 6 && userIdLength <= 16) {
        document.querySelector('.validator.userId').innerHTML = `유효합니다.`;
        document.querySelector('.userId').style.color = `#00C040`;
    } else {
        document.querySelector('.validator.userId').innerHTML = `아이디는 6자리이상 이어야합니다.`;
        document.querySelector('.userId').style.color = `rgba(233 50 35)`;
    }
}
function passwordCheck() {
    const regPassword = /^(?=.*?[0-9a-zA-Z])(?=.*?[#?!@$%^&*-]).{8,}$/;
    if (regPassword.test(inputPassword.value) === true) {
        document.querySelector('.validator.userPassword').innerHTML = `유효합니다.`;
        document.querySelector('.userPassword').style.color = `#00C040`;
    } else {
        document.querySelector('.validator.userPassword').innerHTML = `비밀번호는 8자 이상이어야 하며, 영문/숫자 특수문자를 모두 포함해야 합니다.`;
        document.querySelector('.userPassword').style.color = `rgba(233 50 35)`;
    }
}

function isSameCheck() {
    let pwd = inputPassword.value;
    let cpwd = confrimPassword.value;
    
    if (pwd === cpwd) {
        document.querySelector('.validator.confirmPw').innerHTML = `비밀번호가 일치합니다.`;
        document.querySelector('.confirmPw').style.color = `#00C040`;
    } else {
        document.querySelector('.validator.confirmPw').innerHTML = `비밀번호가 일치하지 않습니다.`;
        document.querySelector('.confirmPw').style.color = `rgba(233 50 35)`;
    }
}


function nameCheck() {
    const regName = /^[가-힣]{2,4}$/;
        if (regName.test(inputUserName.value) === true) {
            document.querySelector('.validator.userName').innerHTML = '유효합니다.';
            document.querySelector('.userName').style.color = `#00C040`;
        } else {
            document.querySelector('.validator.userName').innerHTML = `올바르지 않습니다.`;
            document.querySelector('.userName').style.color = `rgba(233 50 35)`;
        }
}

function yearCheck() {
    const regYear =  /^[0-9]+$/;
        if (regYear.test(inputYear.value) === true) {
            document.querySelector('.validator.userYear').innerHTML = '유효합니다.';
            document.querySelector('.userYear').style.color = `#00C040`;
        } else {
            document.querySelector('.validator.userYear').innerHTML = `올바르지 않습니다.`;
            document.querySelector('.userYear').style.color = `rgba(233 50 35)`;
        }
}


function nicknameCheck() {
    let userNicknameLength = inputUserNickname.value.length;
    if (userNicknameLength >= 2 && userNicknameLength <= 16) {
        document.querySelector('.validator.userNickname').innerHTML = `유효합니다.`;
        document.querySelector('.userNickname').style.color = `#00C040`;
    } else {
        document.querySelector('.validator.userNickname').innerHTML = `유효하지않습니다.`;
        document.querySelector('.userNickname').style.color = `rgba(233 50 35)`;
    }
}



// 이메일 함수
// const regEmail = /^[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_\.]?[0-9a-zA-Z])*\.[a-zA-Z]{2,3}$/;
//     if (regEmail.test(inputUserEmail.value) === true) {
//         document.querySelector('.validator.userEmail').innerHTML = `유효합니다.`;
//         document.querySelector('.userEmail').style.color = `#00C040`;
//     } else {
//         document.querySelector('.validator.userEmail').innerHTML = `이메일 형식이 올바르지 않습니다.`;
//         document.querySelector('.userEmail').style.color = `rgba(233 50 35)`;
//     }
