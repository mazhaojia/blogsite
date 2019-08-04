from database.models.Category import Category


class CategoryOperations:
    @staticmethod
    def add(name):
        category = Category(name=name)
        category.save()

    @staticmethod
    def delete(name):
        categories = Category.objects(name=name)
        if len(categories) == 1:
            category = categories.first()
            category.delete()

    @staticmethod
    def get_category(name):
        categories = Category.objects(name=name)
        if len(categories) == 1:
            category = categories.first()
            return category
        else:
            CategoryOperations.add(name)
            category = Category.objects(name=name).first()
            return category
