//new audio context to help us record 
window.onload = function() {
  var recordButton = $("#recordButton");
  var gumStream;
  //stream from getUserMedia() 
  var rec;
  //Recorder.js object 
  var input;
  //MediaStreamAudioSourceNode we'll be recording 
  // shim for AudioContext when it's not avb. 
  var AudioContext = window.AudioContext || window.webkitAudioContext;
  var audioContext = new AudioContext;

  var constraints = {
    audio: true,
    video: false
  } 

  function startRecording() { 
    console.log("recordButton pressed");
    recordButton.text("Release to stop recording");
    
    navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
      console.log("getUserMedia() success, stream created, initializing Recorder.js ..."); 
      /* assign to gumStream for later use */
      gumStream = stream;
      /* use the stream */
      input = audioContext.createMediaStreamSource(stream);
      /* Create the Recorder object and configure to record mono sound (1 channel) Recording 2 channels will double the file size */
      rec = new Recorder(input, {
          numChannels: 1
      }) 
      //start the recording process 
      rec.record()
      console.log("Recording started");
    });
  }

  function stopRecording() {
    console.log("startButton released");
    recordButton.text("Press to record");

    rec.stop(); //stop microphone access 
    gumStream.getAudioTracks()[0].stop();
    //create the wav blob and pass it on to createDownloadLink 
    // this is for testing 
    rec.exportWAV(createDownloadLink);
    rec.exportWAV(sendToServer); //change this to createDownloadLink for testing
  }

  function sendToServer(blob) {
    console.log(blob);
    socket.emit('audio',  { audio: blob, username});
  }


  function createDownloadLink(blob) {
    var url = URL.createObjectURL(blob);
    var au = document.createElement('audio');
    var li = document.createElement('li');
    var link = document.createElement('a');
    //add controls to the <audio> element 
    au.controls = true;
    au.src = url;
    //link the a element to the blob 
    link.href = url;
    link.download = new Date().toISOString() + '.wav';
    link.innerHTML = link.download;
    //add the new audio and a elements to the li element 
    li.appendChild(au);
    li.appendChild(link);
    //add the li element to the ordered list 
    $('#audio-list')[0].appendChild(li);
  }

  //add events to those 3 buttons 
  recordButton.mousedown(startRecording);
  recordButton.mouseup(stopRecording);

};
