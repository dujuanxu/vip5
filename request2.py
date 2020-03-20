import requests


#request get方法
def get_csdn():
    urlstr = 'https://www.csdn.net/'

    r = requests.get(url=urlstr)
    print(r.text)

#request post方法
def csdn_login():

    urlstr = 'https://passport.csdn.net/v1/register/pc/login/doLogin'
    headers = {'User-Agent': 'Mozilla/6.0'}
    # payload ={"loginType": "1",
    #           "pwdOrVerifyCode": "dujuanxu123",
    #           "userIdentification": "13681589150"
    #           # "uaToken": '122#TwEBGJ+7EEaiBEpZMEpJEJponDJE7SNEEP7rEJ+/f9t/2oQLpo7iEDpWnDEeK51HpyGZp9hBuDEEJFOPpC76EJponDJL7gNpEPXZpJRgu4Ep+FQLpoGUEELWn4yP7SQEEyuLpERBswbLprTTeCOnPKOvwqXnp3XVY9iQeduHJJsdk4ZfpRoQ5uZev3L0JMqf6DkSuGK3I1Jxm/YV0EL7ApfBzsWSonpTo1PTLJ7G2tkSmOEudmXmek3f8K9imDMcW9MBezlYiTPxioI7BqIvs4dYIISgWF9nahgsej6EEa/z8oL6JnipKThDiwL2DEpxneGcQ3MEAqmr8o+UJDEEyB3tqWZ0HsO8ngL4uO8pELVZGWZRfsTbyFfDmSfbEEpMnMp1uOIEELXZ8oL6JNEERBfmqM32E5pangL4ul0EDLVr8CpUJ4bEyNRDqMfVpDpxngLV8Om9E5G+PkoNmzJLKEeVEN06GRkb1xNGLea242iaAx4ppDcx6QyJQqve9q9e2ncHQq/ZlqQGaExOMkwILVvE7qduxxg9dEVUK9kcrdfWnPR0jAXu8LsfBT46+AozDySNe/ZG9WZ4r/FSSNhPB3ZLI2d1cJy1QMGfcVrzCqfvlw9FjXhq9iiEH6zw/+8AIGjCysKEkuNB060skMeVkSzoBHDGfsyL980x6gjB1ZCSs/84D2Rfc5mkrUx7/p7isFEgx57QhD8+mDH46R0lSq8rrr8Z48+bT2ggoIIcQbwouUZUDFODqpyBsHNcxcpN+Tp5/0XI/EfG67xGnbdhdpR5nHIg8jLeuCy+UATD3n02N8gJEz5yMoNhutMq8qXDRPKQkuLDbCu07RfLTpyFJEnveBZJBTGVHPeV+ZZIT91+Qs+YkxJqxxjMByt953PCHiFMh9dNAy6OLQx2b72JkqG6HB1YZdmkecxcnjiKcSqIC4Nd/I8meoX4wxYZWeQOTThIfGiKhC63fWCdBIR5hG93/drYXIgCypuO+3AnSTYukoO2Mkh7kJSuVqtho112fORxt9L+mEoKeFBhhtfg3e/ebUbtLfZYBuR8lpL9Lz/uLZY9mRVfZb7AWkddr6AooR9l409hiNcwxwdxmv0OZW3IPYjA5PD6HX50iHN7IDflISAoa0bjsivQ9oBdcwW7Xrxn+GGiSZw0NIUVUW4cw2H8FKjw2FkBLHC1XBerxx8FlZnF2sDfmKorMhUisIghmHnjHulFCrqxXvIvBpofFlZXNK1wRkbNk/+vSAheqM0rR9CXJep3AbX5nsuEMRYYRGnygoqBtgcepcN5eAX8XjqJ7zxMTBKCCx6CcTxmAweatBgb7NZay2P0HMxhbX4XCemlqx/owKw2a/HQG9kse8djdqmCcQ7GntQFciHzB368fDSLb27jJZax7CHTFrDCkORWmB4KbsWs48F+XfijT+XDQN/ycBww28F3VSmnxNeDeW7vPgWg8gZ72dz/aEt+wTNRNQ2S74lO+12zJ9ptJqoYMOEqFeXxO4==',
    #           # "webUmidToken": "T8237024FBBC1ADBA0BB67C0BEE39BD829B55620EB22136BD0068F04634"
    #             }
    # payload = { "loginType":"1", "pwdOrVerifyCode":"dujuanxu123" }
    payload = {"loginType":"1",
               "pwdOrVerifyCode":"dujuanxu123",
               "userIdentification": "13681589150",
               "uaToken":"122#bHKNYJaeEE+5OJpZMEpJEJponDJE7SNEEP7rEJ+/f9t/2oQLpo7iEDpWnDEeK51HpyGZp9hBuDEEJFOPpC76EJponDJL7gNpEPXZpJRgu4Ep+FQLpoGUEELWn4yP7SQEEyuLpERlsiSWprTTeCOnPKOv6N89kmrYWbH0rL1ukLcduc6Xa9tUbxfYHF49JKoVDyZh6SC0fsR+2qqw9Vyxj2Ap8dqE+mQ9amJFvRb+PBywgqa9Mk7uns5VjUegqelB4NhzSfB84BACIVXt7f97WYrRv5FM6Qp1HNIEEa4I8oL6JRipHHpthn7WDEpxn77c1QDby3AT8o+UJDEEyB3tqWZ0HsO8ngL4uO8pELVZGWZRfsTbyFfDmSfbEEpMnMp1uOIEELXZ8oL6JNEERBfmqM32E5pangL4ul0EDLVr8CpUJ4bEyNRDqMfVpDpxngLV8Om9E5G+PkoNmzJLcJeau3hsGRkb1xNGLea242iaAx4ppDcx6QqkPDj6BDiz1/juDpOdVLBanECzl9kZqzsifmUIjQgrkN+q3ThT/26S2ySS2ZgKcHSTNPrYSK4AnWLHzbg4bNGmv/yIghlqNqjtzOcqwaFyHPbubp1OjkxOp5ePy2q8rzFshLZFZhgh9dCxFw0cHdYqMp/vvlEcvr5izrSPHSguEKHQtLbCCn0PFwhuwCus8DgtQg8Zr/HjiFsoOYqLpKZXfEFo7o+V7aFGD4Xcb33gTL1jB+1Uai1dbFozsFTPLNeZH3AMX73YkZFiArrE5aOUOpQcGPQD6EJhLwrpG6T4k64rF//N1yi9TBwSGQFxNMA8M1J35J8wU5ofOsVKbnnVA5YSOvgz3SySRkGApcPWxQhl1X5mtCQcM5qZ4BZKxQA1cMDCLb3F8IP2naDRoK87OyfhnYKjyo+V8ez9P50wYS5zWos6GsRTlYpGERH6iibB/Sch/w1IHA8iDgCc+JVWfQ/kh6nIyfkt+aUI8xeJpZJ1jQ7cT0B7ztrPqrOhjLffYj6W7cDI0XgIQX2xpVDnwEJ0/ER7JlhJF0qHEr41bUNkJiJLwpxcRmAmdKTNbwJlg1Q3N6iUV6rECiWa0aMrSadrpNq3rw8a8zF3pO1zOv6UnvOF49pzkbpyCwiDxyHqYgT7eSQPdyZzryNduky/fa4eM7BCCreSD5uRIizlj+Ejl9gnpfLqK3ElBRUtWG+MIvQ6kn2qhndIdaJwnbk00fDo4AQwI/Dzdq+lrMj8lqS8i3C0dQrQT13QpdOBIikH0FVkD0HCP30PqckEi1IIIG8qGelimUp0b7N7upcXahiG7Ceu3fDZ7DMo5ifksoJgOcmDhkMvPvWUM9OBhoIKABaMmBIRHMnWjbmGl0TUIpGZbyUXbS8Src7xCDiv+1SINIVgrbf/tr8sa5iLeN9W2JiltwP+xp74o+iZDEgTAnMiNd4k3819RjSJ00L+5iBAxZvdGKEDf6rtmi5BW/9aoPdjPUMOQCdrBFMDqDsVzYZqOtB+LS9UMP8zTFoi3D/DV+rFSAebuMx/rqkod4VMR8S0fKKg9v3YE/c8NCJIg6wM0juhGHUslRSDeAO3aOpp",
               "webUmidToken":"TD02C3CAAFA09FC54B33202107822ECB6A5E432EDDFF21C1A9BA3AEC314"
               }
    r = requests.post(url=urlstr, json=payload, headers=headers )
    print(r.text)



if __name__ == '__main__':
    csdn_login()