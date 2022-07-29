"""
使用ray.tune
"""
import ray
from ray import tune
from ray.tune.schedulers import ASHAScheduler

#
tune.report()


def train_mnist(config):
    # 加载数据
    mnist_transforms = transforms.Compose(
        [transforms.ToTensor(),
         transforms.Normalize((0.1307,), (0.3081,))])

    train_loader = DataLoader(
        datasets.MNIST("~/data", train=True, download=True, transform=mnist_transforms),
        batch_size=64,
        shuffle=True)
    test_loader = DataLoader(
        datasets.MNIST("~/data", train=False, transform=mnist_transforms),
        batch_size=64,
        shuffle=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # 定义模型
    model = ConvNet()
    model.to(device)

    # 优化器
    optimizer = optim.SGD(
        model.parameters(), lr=config["lr"], momentum=config["momentum"])

    # 训练过程
    for i in range(10):
        train(model, optimizer, train_loader)
        acc = test(model, test_loader)

        # 返回当前step验证结果到Ray Tune, 以决定是否停止等后续操作.
        tune.report(mean_accuracy=acc)

        if i % 5 == 0:
            # 保存当前模型文件.
            torch.save(model.state_dict(), "./model.pth")





