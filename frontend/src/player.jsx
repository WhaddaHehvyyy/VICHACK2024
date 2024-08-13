import ReactPlayer from 'react-player';
import './player.css'
import logo from './assets/logo_only.png'
function PlayerScreen() {

    return (
      <>
        <div className='heading-div'>
          <img src={logo} className='logo'></img>
          <h1 className='accu-title'>AccuBoxer AI</h1>
        </div>
        
        <div className='boxing-display'>
          <div className='player-container'>
            <div className='boxer-div'>
              <h1 className='boxer-title'>Boxer 1</h1>
              
            </div>

            <div className='player-div'>

              <ReactPlayer url="https://www.twitch.tv/dinah" height={"70%"} width={"100%"}  style={{ borderRadius: '10px', overflow: 'hidden' }}/>
              <div className='button-div'>
                <button className='frame-button'>Show Frames</button>

              </div>
              
            </div>

            <div className='boxer-div'>
              <h1 className='boxer-title'>Boxer 2</h1>
            </div>

          </div>
          

          

          
        </div>
        
      </>
    )
  }

  export default PlayerScreen