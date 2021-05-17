const fs = require('fs');
const crypto = require('crypto');
const express = require('express');

exports.dec = (req, res) => {
    //{ date: '2021-05-15', time: '21:58' }
    console.log(req.body);
    const date = req.body.date;
    const time = req.body.time;
    const dateArr = date.split("-");
    const timeArr = time.split(":");

    // 암호화 키
    const key = Buffer.from('00112233445566778899aabbccddeeff', 'hex');
    // number used once 매번 바꿔 사용하는 번호 
    const nonce = Buffer.from('112233445566778899aabbcc', 'hex');
    // Addtional Associated Data : https://cloud.google.com/kms/docs/additional-authenticated-data
    const aad = Buffer.from('0102030405060708090a0b0c0d0e', 'hex');
    var ciphertext = Buffer.from(fs.readFileSync("C:/opencv/" + dateArr[1] + "m" + dateArr[2] + "/" + timeArr[0] + "." + timeArr[1] + ".bin"), 'hex');
    //var ciphertext = Buffer.from(fs.readFileSync("'C:/opencv/05m15/21.58.bin'), 'hex');
    var mac = Buffer.from('236f7a81ffe4ea68f4b9f70377c46955', 'hex');
    //var mac = Buffer.from('db 로부터 가져오기', 'hex');

    // 키 정보 출력

    //console.log('ciphertext: ' + ciphertext.toString('hex'));
    console.log('key:' + key.toString('hex'));
    console.log('nonce:' + nonce.toString('hex'));
    console.log('add: ' + aad.toString('hex'));
    console.log('mac: ' + mac.toString('hex'));
    const plaintext = decryption(key, nonce, aad, ciphertext, mac);
    console.log(plaintext)

    var imgsrc = "data:image/bmp;base64," + plaintext;

    res.render('main', { imgsrc: imgsrc });
}

function decryption(key, nonce, aad, ciphertext, tag) {
    // 암호화 객체 생성 (key와 nonce 추가)
    const decipher = crypto.createDecipheriv('aes-128-gcm', key, nonce, {
        authTagLength: 16
    });

    // 태그 추가
    decipher.setAuthTag(tag);
    // aad 추가
    decipher.setAAD(aad, {
        plaintextLength: ciphertext.length
    });

    // 복호화 시작!
    const receivedPlaintext = decipher.update(ciphertext);

    try {
        // 복호화 완료 - 더 이상 복호화 할 수 없음.
        const dex = decipher.final();
        return receivedPlaintext;
    } catch (err) {
        console.log(err);
        console.error('Authentication failed!');
        return;
    }
}
