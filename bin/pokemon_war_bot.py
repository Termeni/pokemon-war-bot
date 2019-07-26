import game_manager
import twitter_client
import image_generator

def main():
    if game_manager.is_playable():
        result = game_manager.play()
        image_generator.update_status_images(result)
        twitter_client.publish_status(result)
        if game_manager.has_ended():
            winner = game_manager.get_winner()
            twitter_client.publish_winner(winner)

main()
