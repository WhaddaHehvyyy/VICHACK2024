import ReactPlayer from 'react-player';
import './player.css'

function PlayerScreen() {

    return (
      <>
        <h1 className='andy'>AccuBoxer AI</h1>
        <div className='player-div'>
            <ReactPlayer url="https://www.twitch.tv/lck" height={"70%"} width={"60%"}/>
            
        </div>
        
      </>
    )
  }

  export default PlayerScreen