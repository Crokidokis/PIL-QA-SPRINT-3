class Login:
    btn_login_xpath = '//*[@id="headerSamsung"]/div[2]/div/div/div/div/div[2]/ul[2]/li[1]/a'
    txt_email_xpath = '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/form/div[1]/label/div/input'
    btn_password_xpath = '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div/form/div[2]/div/label/div/input'
    btn_enter_xpath = '//span[contains(text(),"Entrar")]'
    profile_xpath = '/html/body/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div/section/header/div[2]/div/div/div[1]'
    btn_home_xpath = '//*[@id="headerSamsung"]/div[2]/div/div/a'
    #LINKS
    link_login = 'https://shop.samsung.com/ar/login?returnUrl=%2Far%2Faccount'
    link_profile = 'https://shop.samsung.com/ar/account#/profile'