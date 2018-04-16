# FilmaffinityProTrends
Filmaffinity Professional Reviews Trends
# ![image](http://www.saidaonline.com/en/newsgfx/pop-corn-movies-saidaonline.jpg)

**Prerequisites**

_Any csv Reader_
_Python 3. * with the following libraries:_

`pip install csv`

`pip install requests`

`pip install lxml`

`pip install beautifulsoup4`

**The Dataset**

_This Dataset in **csv** format separated by semicolons i contains a tendency of a review extracted from the Filmaffinity website in each record. The trends can be positive, neutral, or negative. In addition, it includes in each record: the title, the year of publication of the film, the distribution of actors, as well as the author of the review and the medium where it was published._

_The purpose of having extracted these data is to be able to perform a statistical analysis through which to create clusterings, in addition to analyzing whether the different variables are dependent. Trying to find out for example, if the cast, the actor or the director of the review are determining factors._

_As a future work, it would be interesting to create a relational database, in which also add factors such as the budget for creation, the income generated and even the criticism of web users. It could also be revealing to contrast with other similar websites._

_It would also be nice to write an sript with which to update the data without having to download the existing ones._

Note: To make the file lighter some criticisms have been ignored. However, if you want to get all the criticism you can run the script - take special care in how to set the time.sleep or you will be banned from Filmaffinity-. The validity of the data, given its nature is persistent, but requires daily updating.

**The Script**

_This work also includes the script through which the data has been obtained. The script is programmed in **python** and makes extensive use of **beautifulsoup** library._

_Basically we must control the **MAX_REGS** variable from which we control the maximum number of records that we want our data set to have. There are also some time.sleep declared to control the amount of url we request per second, in order to avoid being banned._

Fields:

Pelicula: The Name of the Movie.
Date: The Year of Release.
Duracio: The duration in min.
Director: Name Of the director.
Genre: The Genere.
Autor: The Author of Review.
Medi: Where the review has published.
Tendencia: Trend of the review.
Actors: The Cast Of the Movie.

**Inspiration**

_As a lover of the seventh art, I have always asked myself questions of the style:_

-What factors are what make a movie like it or not?

-That a director gets good reviews is synonymous with benefits?

-Does the distribution influence the critical tendency?

-To what extent does professional criticism coincide with that of the rest of mortals?

-The logic makes me think that being a major critical mass is more profitable to focus

-the movies to the non-professional sector. Is this true?

-etc.

_To answer these questions it would be necessary to populate our set with data referring to the economic part. Also I think it is necessary to create a good design to be able to make massive consultations. However, I believe that this practice can be a good start._

_I think that these types of questions could generate algorithms that respond to commercial purposes to maximize benefits. These algorithms could easily be exported to all types of products not necessarily related to the cinema._

**Thanks.**

_All the data in this dataset are public and are obtained from the Filmaffinity website. I want to thank the filaffinity website for its great work both as a directory of movies, as a repository of reviews, as well as creating a community where movie lovers can consult and interact._

_**License**_

_I have decided to license this repository under **Released Under CC0: Public Domain License**, since, the data are not proprietary they are public, they do not contain author rights, since, the criticism is not included, only the tendency. I also think it is interesting that if someone wants to use the code or data set included in this repository, they can do it without any kind of restriction, or have to name the original work, since this does not have any remarkable peculiarity that can not have another similar . Also, in my opinion, to share is to live._
