// Zyrox Proxy with Playwright: one IP per browser context.
import { chromium } from 'playwright'

const { ZYROX_USER, ZYROX_PASS } = process.env

const browser = await chromium.launch()

for (const name of ['visitor1', 'visitor2']) {
  const context = await browser.newContext({
    proxy: {
      server: 'http://host.zyroxproxy.com:7000',
      username: `${ZYROX_USER}-country-us-session-${name}`,
      password: ZYROX_PASS,
    },
  })
  const page = await context.newPage()
  await page.goto('https://api.ipify.org')
  console.log(name, await page.textContent('body'))
  await context.close()
}

await browser.close()
