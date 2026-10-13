// Zyrox Proxy with Node.js fetch (Node 18+).
// Node's built-in fetch ignores the `agent` option, so use undici's
// ProxyAgent as the `dispatcher` instead.
import { ProxyAgent, fetch } from 'undici'

const { ZYROX_USER, ZYROX_PASS } = process.env
const HOST = 'host.zyroxproxy.com:7000'

// Options ride in the username as -key-value pairs.
const proxyUrl = (params = {}) => {
  const user = ZYROX_USER + Object.entries(params).map(([k, v]) => `-${k}-${v}`).join('')
  return `http://${user}:${ZYROX_PASS}@${HOST}`
}

async function getIp(url) {
  const res = await fetch('https://api.ipify.org', { dispatcher: new ProxyAgent(url) })
  return res.text()
}

console.log('Rotating:     ', await getIp(proxyUrl()), await getIp(proxyUrl()))
console.log('United States:', await getIp(proxyUrl({ country: 'us' })))

const sticky = proxyUrl({ country: 'de', session: 'node1', sessiontime: 60 })
console.log('Sticky (DE):  ', await getIp(sticky), await getIp(sticky))
