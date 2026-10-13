// Zyrox Proxy with Puppeteer. Chrome needs only host:port; credentials go
// through page.authenticate(), which you must call on EVERY new page.
import puppeteer from 'puppeteer'

const { ZYROX_USER, ZYROX_PASS } = process.env

const browser = await puppeteer.launch({
  args: ['--proxy-server=http://host.zyroxproxy.com:7000'],
})

const page = await browser.newPage()
await page.authenticate({
  username: `${ZYROX_USER}-country-us-session-pptr1`,
  password: ZYROX_PASS,
})

await page.goto('https://api.ipify.org')
console.log('Exit IP:', await page.evaluate(() => document.body.innerText))
await browser.close()
