
const APP_ID = process.env.APP_ID_AGORA
// const TOKEN = sessionStorage.getItem('token')
// const CHANNEL = sessionStorage.getItem('room')


// let UID = sessionStorage.getItem('UID')

// let NAME = sessionStorage.getItem('name')

// const client = AgoraRTC.createClient({mode:'rtc', codec:'vp8'})

// let localTracks = []
// let remoteUsers = {}
const urlParams = new URLSearchParams(window.location.search);
const TOKEN = urlParams.get('token');  // Get token from the URL
const CHANNEL = urlParams.get('room');  // Get room name from the URL
let UID = urlParams.get('uid');  // Get UID from the URL
let NAME = sessionStorage.getItem('name');


let joinAndDisplayLocalStream = async () => {
    document.getElementById('room-name').innerText = CHANNEL

    client.on('user-published', handleUserJoined)
    client.on('user-left', handleUserLeft)

    try{
        UID = await client.join(APP_ID, CHANNEL, TOKEN, UID)
    }catch(error){
        console.error(error)
        window.open('/', '_self')
    }
    
    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let member = await createMember()

    let player = `<div  class="video-container" id="user-container-${UID}">
                     <div class="video-player" id="user-${UID}"></div>
                     <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
                  </div>`
    
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
    localTracks[1].play(`user-${UID}`)
    await client.publish([localTracks[0], localTracks[1]])
}

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    if (mediaType === 'video'){
        let player = document.getElementById(`user-container-${user.uid}`)
        if (player != null){
            player.remove()
        }

        let member = await getMember(user)

        player = `<div  class="video-container" id="user-container-${user.uid}">
            <div class="video-player" id="user-${user.uid}"></div>
            <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
        </div>`

        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
        user.videoTrack.play(`user-${user.uid}`)
    }

    if (mediaType === 'audio'){
        user.audioTrack.play()
    }
}

let handleUserLeft = async (user) => {
    delete remoteUsers[user.uid]
    document.getElementById(`user-container-${user.uid}`).remove()
}



let toggleCamera = async (e) => {
    try {
        if (localTracks[1].muted) {
            await localTracks[1].setMuted(false);
            e.target.style.backgroundColor = '#fff';
        } else {
            await localTracks[1].setMuted(true);
            e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)';
        }
    } catch (error) {
        console.error('Error toggling camera:', error);
    }
}


let toggleMic = async (e) => {
    console.log('TOGGLE MIC TRIGGERED')
    if(localTracks[0].muted){
        await localTracks[0].setMuted(false)
        e.target.style.backgroundColor = '#fff'
    }else{
        await localTracks[0].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}

let createMember = async () => {
    let response = await fetch('/create_member/', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'name':NAME, 'room_name':CHANNEL, 'UID':UID})
    })
    let member = await response.json()
    return member
}


let getMember = async (user) => {
    let response = await fetch(`/get_member/?UID=${user.uid}&room_name=${CHANNEL}`)
    let member = await response.json()
    return member
}

let deleteMember = async () => {
    let response = await fetch('/delete_member/', {  
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'name': NAME, 'room_name': CHANNEL, 'UID': UID })
    });
    let member = await response.json();
}

let leaveAndRemoveLocalStream = async () => {
    try {
        // Stop and close local tracks
        for (let i = 0; localTracks.length > i; i++) {
            localTracks[i].stop();
            localTracks[i].close();
        }

        // Leave the channel
        await client.leave();

        // Call deleteMember explicitly when the user leaves
        await deleteMember();

        // Redirect the user to the homepage
        window.open('/', '_self');
    } catch (error) {
        console.error("Error during leave: ", error);
    }
};


window.addEventListener("beforeunload",deleteMember);

joinAndDisplayLocalStream()

document.getElementById('leave-btn').addEventListener('click', leaveAndRemoveLocalStream)
document.getElementById('camera-btn').addEventListener('click', toggleCamera)
document.getElementById('mic-btn').addEventListener('click', toggleMic)

