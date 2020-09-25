
/**
 * This library uses a websocket URL to connect to
 * the webd network. This has several limitations:
 *  - Require a peer to proxy reads/writes to non-websocket peers
 *  - Cannot create a share (no filesystem, no UDP, no websocket server capability)
 *  - Writes are limited to one file at a time
 * 
 * Despite being limited it still may be useful to
 * talk to the webd network from a html UI, for purposes like
 * reading files on a laptop from a phone.
 */



