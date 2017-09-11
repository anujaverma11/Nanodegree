# Calling Class
# Movie is a class defined in media.py

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

minions = media.Movie("Minions",
                        "Minions are small, yellow creatures who have existed since the beginning of time, evolving from single-celled organisms into beings who exist only to serve history's most despicable masters",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",
                        "https://www.youtube.com/watch?v=eisKxhjBnZ0")

tangled = media.Movie("Tangled",
                      "The story of a lost, young princess with long magical hair who yearns to leave her secluded tower. Against her mother's wishes, she accepts the aid of a handsome intruder to take her out into the world which she has never seen.",
                      "https://upload.wikimedia.org/wikipedia/en/a/a8/Tangled_poster.jpg",
                      "https://www.youtube.com/watch?v=JYKpIr1lSG0")

frozen = media.Movie("Frozen",
                      "The story of a fearless princess who sets off on a journey alongside a rugged iceman, his loyal pet reindeer, and a naive snowman to find her estranged sister, whose icy powers have inadvertently trapped the kingdom in eternal winter.",
                      "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",
                      "https://www.youtube.com/watch?v=TbQm5doF_Uc")

theJungleBook = media.Movie("The Jungle Book",
                      "The story of Mowgli, an orphaned human boy who, guided by his animal guardians, sets out on a journey of self-discovery while evading the threatening Shere Khan.",
                      "https://upload.wikimedia.org/wikipedia/en/a/a4/The_Jungle_Book_%282016%29.jpg",
                      "https://www.youtube.com/watch?v=5mkm22yO-bs")

findingNemo = media.Movie("Finding Nemo",
                      "The story of the overprotective Ocellaris clownfish named Marlin who, along with a regal blue tang named Dory, searches for his abducted son Nemo all the way to Sydney Harbour. ",
                      "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
                      "https://www.youtube.com/watch?v=2zLkasScy7A")

# tangled.show_trailer()
moview = [toy_story, minions, tangled, frozen, theJungleBook, findingNemo]
fresh_tomatoes.open_movies_page(moview) # open_movies_page is a function defined in fresh_tomatoes

print(media.Movie.__doc__) # This line will print all the statements written as __doc__ in Movie class