
fn main() {
    // check for server, if none fork and re-execute
    
    // check if we should become server + do so

    // act as client

    // parse args:
    //   ls/read/write

    println!("Hello, world!");


}

fn server_main() {
    // read /etc/webd/webd.toml, ~/.config/webd/webd.toml, %appdata%/webd.toml

    // Now that we have config:
    //  t1: list all configured local directories + their share names
    //  t2: setup our crypto ID in /etc/webd/id.* OR ~/.config/webd/id.* ; generate OR use https://github.com/mozilla/authenticator-rs for FIDO tokens
    //      read in aliases from webd.toml which map nice names -> crypto IDs
    //  t3: multicast for local peers,
    //  t4: make UDP connections to well-nown peers,
    //  t5: poll http[s]:// endpoints for lists of peers,

    // When we connect to a peer:
    //   tell them our ID
    //   receive their ID
    //   ask them what shares they know about (shares have peer data on them)
    //   possibly list files in share


    // when we receive a peer conn:
    //   receive their ID
    //   tell them our ID
    //   wait for commands + execute them





}
