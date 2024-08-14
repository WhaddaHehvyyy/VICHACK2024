import './player.css'
import logo from './assets/logo_only.png'
import { useGlobalState } from './GlobalContext';


function PlayerScreen() {

    const { globalState } = useGlobalState();


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
                    {globalState ? (
              <video controls height='70%' width='100%'>
                <source src={URL.createObjectURL(globalState)} type="video/mp4" />
                Your browser does not support the video tag.
              </video>
            ) : (
              <p>No video file selected.</p>
            )}

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